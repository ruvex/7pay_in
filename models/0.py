# -*- coding: utf-8 -*-

from gluon.custom_import import track_changes; track_changes(True)

### тут еще сессия не задана!!! что конектимся к кукиясам - она в ДВ открывается
### поэтому все операции с сессией в файле ниже ДБ

##if request.is_https:
##    redirect(URL(args=request.args, vars=request.vars, scheme='http', host=True))

from gluon import current
current.CODE_UTF = 'utf8' #'cp1251'
current.PARTNER_MIN = PARTNER_MIN = 10
PARTNER_GO = 77
CACHE_EXP_TIME = request.is_local and 5 or 360

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

DEVELOP = myconf.take('app.develop', cast=bool)

USE_TO_PHONE =  myconf.take('mode.use_to_phone')
USE_EXCHANGE =  myconf.take('mode.use_exchange')
USE_BUY_SELL =  myconf.take('mode.use_buy_sell')
USE_TO_DEALS =  myconf.take('mode.use_to_deals')

TO_BUY_ID = myconf.take('deals.buy')
TO_WALLET_ID = myconf.take('deals.wallet')
TO_COIN_ID = myconf.take('deals.coin')
TO_PHONE7_ID = myconf.take('deals.phone_7')

CURR_USD_ID = myconf.take('currs.usd_id')
CURR_RUB_ID = myconf.take('currs.rub_id')
CURR_BTC_ID = myconf.take('currs.btc_id')

TRUST_IP = myconf.take('app.trust_ip')


if DEVELOP: print '0.py - app.DEVELOP'

current.IS_LOCAL = IS_LOCAL = request.is_local
current.IS_MOBILE = IS_MOBILE = request.user_agent().is_mobile
current.IS_TABLET = IS_TABLET = request.user_agent().is_tablet


ADMIN = request.controller == 'appadmin'
##print ADMIN
SKIN = myconf['skin']

def _get_bon():
    # тут они все строковые так что надо там их преобразовывать
    return {
        'new': myconf.take('bonuses.new', cast=int),
        'gc': myconf.take('bonuses.gc', cast=int),
        'visit': myconf.take('bonuses.visit', cast=int),
        'wait': myconf.take('bonuses.wait', cast=int),
        }
BONUSES = None

if request.ajax:
    pass
else:
    LANGS = {
        'ru': ['Русский', 'ru.png'],
        'en': ['English', 'gb.png'],
        'de': ['Deutsche ', 'de.png'],
        'tr': ['Türkçe', 'tr.png'],
    }

if request.controller == 'bonuses':
    # передадим описатель бонусов
    BONUSES = _get_bon()
