import requests
import json
url = 'https://api.yangkeduo.com/api/caterham/query/fenlei_gyl_group?size=50&opt_name=%E6%89%8B%E6%9C%BA&offset=0&sort_type=DEFAULT&flip=null&list_id=1543_54a13dbd80&opt_type=1&support_types=0_3&opt_id=1543&pdduid=4116564574'
headers = {
    'User-Agent': 'android Mozilla/5.0 (Linux; Android 5.1.1; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36  phh_android_version/4.60.0 phh_android_build/d28e9052b22480bbe393536f9be43f829b6d4c25 phh_android_channel/yyb',
    'Referer': 'Android',
    'Cookie': 'api_uid=rBQHkV0HM8pX4m/58yMRAg=='
}

data = requests.get(url=url,headers = headers,verify = False)
# print(data.text)
info = json.loads(data.text)
# print(info['list'])
for item in info['list']:
    id = item['goods_id']
    name = item['goods_name']
    price = item['price']
    sale = item['sales']
    print(id,name,price,sale)
    pass
