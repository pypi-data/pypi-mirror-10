#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bts_tools - Tools to easily manage the bitshares client
# Copyright (c) 2014 Nicolas Wack <wackou@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from . import core
from collections import deque
from bs4 import BeautifulSoup
import threading
import requests
import functools
import logging

log = logging.getLogger(__name__)

"""BitAssets for which we check and publish feeds."""
BIT_ASSETS = {'USD', 'CNY', 'BTC', 'GOLD', 'EUR', 'GBP', 'CAD', 'CHF', 'HKD', 'MXN',
              'RUB', 'SEK', 'SGD', 'AUD', 'SILVER', 'TRY', 'KRW', 'JPY', 'NZD'}

BIT_ASSETS_INDICES = {'SHENZHEN': 'CNY',
                      'SHANGHAI': 'CNY',
                      'NASDAQC': 'USD',
                      'NIKKEI': 'JPY',
                      'HANGSENG': 'HKD'}

"""List of feeds that should be shown on the UI and in the logs. Note that we
always check and publish all feeds, regardless of this variable."""
DEFAULT_VISIBLE_FEEDS = ['USD', 'BTC', 'CNY', 'GOLD', 'EUR']

feeds = {}
nfeed_checked = 0
cfg = None
history_len = None
price_history = None
visible_feeds = DEFAULT_VISIBLE_FEEDS


def load_feeds():
    global cfg, history_len, price_history, visible_feeds
    cfg = core.config['monitoring']['feeds']
    history_len = int(cfg['median_time_span'] / cfg['check_time_interval'])
    price_history = {cur: deque(maxlen=history_len) for cur in BIT_ASSETS | set(BIT_ASSETS_INDICES.keys())}
    visible_feeds = cfg.get('visible_feeds', DEFAULT_VISIBLE_FEEDS)



def check_online_status(f):
    @functools.wraps(f)
    def wrapper(self, *args, **kwargs):
        try:
            result = f(self, *args, **kwargs)
        except Exception:
            if FeedProvider.PROVIDER_STATES.get(self.NAME) != 'offline':
                log.warning('Feed provider %s just went offline' % self.NAME)
                FeedProvider.PROVIDER_STATES[self.NAME] = 'offline'
            raise
        else:
            if FeedProvider.PROVIDER_STATES.get(self.NAME) != 'online':
                log.info('Feed provider %s came online' % self.NAME)
                FeedProvider.PROVIDER_STATES[self.NAME] = 'online'
        return result
    return wrapper


class FeedProvider(object):
    NAME = 'base FeedProvider'
    PROVIDER_STATES = {}

    def __init__(self):
        self.state = 'offline'


class YahooProvider(FeedProvider):
    NAME = 'Yahoo'
    _YQL_URL = 'http://query.yahooapis.com/v1/public/yql'
    _YAHOO_BTS_MAP = {'GOLD': 'XAU',
                      'SILVER': 'XAG',
                      'SHENZHEN': '399106.SZ',
                      'SHANGHAI': '000001.SS',
                      'NIKKEI': '^N225',
                      'NASDAQC': '^IXIC',
                      'HANGSENG': '^HSI'}

    @staticmethod
    def to_bts(c):
        c = c.upper()
        for b, y in YahooProvider._YAHOO_BTS_MAP.items():
            if c == y:
                return b
        return c

    @staticmethod
    def from_bts(c):
        c = c.upper()
        return YahooProvider._YAHOO_BTS_MAP.get(c, c)

    @check_online_status
    def query_yql(self, query):
        r = requests.get(self._YQL_URL,
                         params=dict(q = query,
                                     env = 'http://datatables.org/alltables.env',
                                     format='json')).json()
        try:
            return r['query']['results']['quote']
        except KeyError:
            return r

    def query_quote_full(self, q):
        log.debug('checking quote for %s at Yahoo' % q)
        r = self.query_yql('select * from yahoo.finance.quotes where symbol in ("{}")'.format(self.from_bts(q)))
        return r

    def query_quote(self, q):
        # Yahoo seems to have a bug on Shanghai index, use another way
        if q == 'SHANGHAI':
            log.debug('checking quote for %s at Yahoo' % q)
            r = requests.get('http://finance.yahoo.com/q?s=000001.SS')
            soup = BeautifulSoup(r.text)
            r = float(soup.find('span', 'time_rtq_ticker').text.replace(',', ''))
        else:
            r = float(self.query_quote_full(q)['LastTradePriceOnly'])
        return r

    @check_online_status
    def get(self, asset_list, base):
        log.debug('checking feeds for %s / %s at Yahoo' % (' '.join(asset_list), base))
        asset_list = [self.from_bts(asset) for asset in asset_list]
        base = base.upper()
        query_string = ','.join('%s%s=X' % (asset, base) for asset in asset_list)
        r = requests.get('http://download.finance.yahoo.com/d/quotes.csv',
                         timeout=60,
                         params={'s': query_string, 'f': 'l1', 'e': 'csv'})

        asset_prices = map(float, r.text.split())
        return dict(zip((self.to_bts(asset) for asset in asset_list), asset_prices))


class BterFeedProvider(FeedProvider):
    NAME = 'Bter'

    @check_online_status
    def get(self, cur, base):
        log.debug('checking feeds for %s/%s at %s' % (cur, base, self.NAME))
        r = requests.get('http://data.bter.com/api/1/ticker/%s_%s' % (cur.lower(), base.lower()),
                         timeout=60).json()
        price = float(r['last']) or ((float(r['sell']) + float(r['buy'])) / 2)
        volume = float(r['vol_%s' % cur.lower()])
        return price, volume


class Btc38FeedProvider(FeedProvider):
    NAME = 'Btc38'

    @check_online_status
    def get(self, cur, base):
        log.debug('checking feeds for %s/%s at %s' % (cur, base, self.NAME))
        headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        r = requests.get('http://api.btc38.com/v1/ticker.php',
                         timeout=60,
                         params={'c': cur.lower(), 'mk_type': base.lower()},
                         headers=headers)
        try:
            # see: http://stackoverflow.com/questions/24703060/issues-reading-json-from-txt-file
            r.encoding = 'utf-8-sig'
            r = r.json()
        except ValueError:
            log.error('Could not decode response from btc38: %s' % r.text)
            raise
        price = float(r['ticker']['last']) # TODO: (bid + ask) / 2 ?
        volume = float(r['ticker']['last']) * float(r['ticker']['vol'])
        return price, volume


def weighted_mean(l):
    """return the weighted mean of a list of [(value, weight)]"""
    return sum(v[0]*v[1] for v in l) / sum(v[1] for v in l)


def adjust(v, r):
    return v[0]*r, v[1]*r


def get_feed_prices():
    # doesn't include:
    # - BTC as we don't get it from yahoo
    # - USD as it is our base currency
    yahoo = YahooProvider()
    yahoo_curs = BIT_ASSETS - {'BTC', 'USD'}

    # 1- get the BitShares price in BTC using the biggest markets: USD and CNY

    # first get rate conversion between USD/CNY from yahoo and CNY/BTC from
    # bter and btc38 (use CNY and not USD as the market is bigger)

    yahoo_prices = yahoo.get(yahoo_curs, 'USD')
    cny_usd = yahoo_prices.pop('CNY')

    feed_providers = [BterFeedProvider(), Btc38FeedProvider()]

    feeds_btc_cny = []
    for provider in feed_providers:
        try:
            feeds_btc_cny.append(provider.get('BTC', 'CNY'))
        except:
            pass
    if not feeds_btc_cny:
        raise core.NoFeedData('Could not get any BTC/CNY feeds')
    btc_cny = weighted_mean(feeds_btc_cny)
    cny_btc = 1 / btc_cny

    # then get the weighted price in btc for the most important markets
    feeds_btc = []
    for provider in feed_providers:
        try:
            feeds_btc.extend([provider.get('BTS', 'BTC'),
                              adjust(provider.get('BTS', 'CNY'), cny_btc)])
        except:
            pass
    if not feeds_btc:
        raise core.NoFeedData('Could not get any BTS/BTC feeds')
    btc_price = weighted_mean(feeds_btc)

    cny_price = btc_price * btc_cny
    usd_price = cny_price * cny_usd

    feeds['USD'] = usd_price
    feeds['BTC'] = btc_price
    feeds['CNY'] = cny_price

    # 2- now get the BitShares price in all other required currencies
    for cur, yprice in yahoo_prices.items():
        feeds[cur] = usd_price / yprice

    # 3- get the feeds for major composite indices
    for idx, cur in BIT_ASSETS_INDICES.items():
        feeds[idx] = feeds[cur] / yahoo.query_quote(idx)

    # 4- update price history for all feeds
    for cur, price in feeds.items():
        price_history[cur].append(price)


def median(cur):
    p = price_history[cur]
    return sorted(p)[len(p)//2]


def format_qualifier(c):
    if c in {'BTC', 'GOLD', 'SILVER'} | set(BIT_ASSETS_INDICES.keys()):
        return '%g'
    return '%f'


def check_feeds(nodes):
    # TODO: update according to: https://bitsharestalk.org/index.php?topic=9348.0;all
    global nfeed_checked
    feed_period = int(cfg['publish_time_interval'] / cfg['check_time_interval'])

    try:
        get_feed_prices()
        nfeed_checked += 1

        def fmt(feeds):
            fmt = ', '.join('%s %s' % (format_qualifier(c), c) for c in visible_feeds)
            msg = fmt % tuple(feeds[c] for c in visible_feeds)
            return msg

        log.debug('Got feeds: %s  [%d/%d]' % (fmt(feeds), nfeed_checked, feed_period))

        for node in nodes:
            # if an exception occurs during publishing feeds for a delegate (eg: standby delegate),
            # then we should still go on for the other nodes (and not let exceptions propagate)
            try:
                # only publish feeds if we're running a delegate node
                # we also require rpc_host == 'localhost', we don't want to publish on remote
                # nodes (while checking on them, for instance)
                # TODO: do we really want to ignore rpc_host != 'localhost', or should we just do what is asked?
                if node.type == 'delegate' and node.rpc_host == 'localhost' and 'feeds' in node.monitoring:
                    if nfeed_checked % feed_period == 0:
                        if not node.is_online():
                            log.warning('Cannot publish feeds for delegate %s: client is not running' % node.name)
                            continue
                        if not node.get_info()['wallet_unlocked']:
                            log.warning('Cannot publish feeds for delegate %s: wallet is locked' % node.name)
                            continue
                        # publish median value of the price, not latest one
                        median_feeds = {c: median(c) for c in feeds}
                        log.info('Node %s publishing feeds: %s' % (node.name, fmt(median_feeds)))
                        feeds_as_string = [(cur, '{:.10f}'.format(price)) for cur, price in median_feeds.items()]
                        node.wallet_publish_feeds(node.name, feeds_as_string)
            except Exception as e:
                log.exception(e)

    except core.NoFeedData as e:
        log.warning(e)

    except Exception as e:
        log.exception(e)

    threading.Timer(cfg['check_time_interval'], check_feeds, args=(nodes,)).start()
