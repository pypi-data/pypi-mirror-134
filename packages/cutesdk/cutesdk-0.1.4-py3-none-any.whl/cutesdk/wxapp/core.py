import requests
from cutesdk.wxapp.token import get_access_token
from cutesdk.wxapp.cache import DefaultCache

ACCESS_TOKEN = 'access_token'


class WxApp:

    API_BASE_URI = 'https://api.weixin.qq.com'

    def __init__(self, appid, app_secret):
        self.appid = appid
        self.app_secret = app_secret
        self.cache = DefaultCache()

    def code2session(self, code):
        api_path = '/sns/jscode2session'
        params = {
            'appid': self.appid,
            'secret': self.app_secret,
            'js_code': code,
            'grant_type': 'authorization_code',
        }

        return self.api_get(api_path, params)

    def get_access_token(self):
        api_path = '/cgi-bin/token'
        params = {
            'grant_type': 'client_credential',
            'appid': self.appid,
            'secret': self.app_secret,
        }

        return self.api_get(api_path, params)

    def api_get(self, api_path, params={}):
        api_url = self.API_BASE_URI + api_path

        if 'access_token' in params and params['access_token'] == ACCESS_TOKEN:
            try:
                access_token = get_access_token(self)
                params['access_token'] = access_token
            except Exception as err:
                return {
                    'errcode': -1,
                    'errmsg': str(err)
                }

        res = requests.get(api_url, params=params)

        return res.json()

    def api_post(self, api_path, params={}, data={}):
        api_url = self.API_BASE_URI + api_path

        if 'access_token' in params and params['access_token'] == ACCESS_TOKEN:
            try:
                access_token = get_access_token(self)
                params['access_token'] = access_token
            except Exception as err:
                return {
                    'errcode': -1,
                    'errmsg': str(err)
                }
        res = requests.post(api_url, params=params, json=data)

        return res.json()
