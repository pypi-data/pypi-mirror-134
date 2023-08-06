import hashlib
import json

from cutesdk.wxapp.cache import ICache, DefaultCache

"""default handler defined how to get access_token

:param app: instance of .core.WxApp

:returns: access_token 
"""
def get_access_token(app):
    # get from cache
    key = get_access_token_cache_key(app)
    cache_data = app.cache.get(key)

    # found access_token in cache
    if cache_data is not None and cache_data != '':
        return cache_data
        
    # request api to get access_token
    res = app.get_access_token()
    if res.get('access_token') is not None and res.get('access_token') != '':
        cache_data = res.get('access_token')
        expire = res.get('expires_in') - 300

        # set access_token to cache
        app.cache.set(key, cache_data, expire)

        return cache_data

    # can't get access_token
    if res.get('errmsg') is not None:
        raise Exception('{}-{}', res.get('errcode'), res.get('errmsg')) 

    raise Exception('get access_token failed')

def get_access_token_cache_key(app):
    prefix = 'cutesdk.wxapp.access_token.'
    payload = 'grant_type=client_credential&appid={}&secret={}'.format(app.appid, app.app_secret)
    
    m = hashlib.md5(payload.encode("utf-8")).hexdigest()

    return prefix + m