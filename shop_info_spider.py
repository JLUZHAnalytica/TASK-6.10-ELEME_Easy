import json
import urllib.request

def get_record(store_id):
    url = 'https://h5.ele.me/pizza/shopping/restaurants/%s/batch_shop?' % (shop_id)
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json


