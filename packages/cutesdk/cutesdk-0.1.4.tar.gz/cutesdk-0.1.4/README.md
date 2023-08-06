# cutesdk

## Quick Start

- install cutesdk

```shell
pip install --upgrade cutesdk
```

- use wxapp sdk

when you want to request a wxapp api such as: [analysis.getDailyRetain](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-retain/analysis.getDailyRetain.html)

you can code in python like below:

```python
from cutesdk.wxapp import WxApp, ACCESS_TOKEN

sdk = WxApp(
    appid='xxx', 
    app_secret='xxx',
)

api_path = '/datacube/getweanalysisappiddailyretaininfo'
params = {
    'access_token': ACCESS_TOKEN,
}
data = {
    'begin_date': '20220102',
    'end_date': '20220102',
}

res = sdk.api_post(api_path, params, data)

print(res)
```

