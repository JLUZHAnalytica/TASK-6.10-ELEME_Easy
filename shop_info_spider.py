def get_shop_detail(shop_id):
    url = 'https://h5.ele.me/pizza/shopping/restaurants/' + shop_id + '/batch_shop?extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D'
    try:
        response = requests.get(url, headers=headers)
        print('详情页')
        html_str = response.text
    except Exception:
        print('报错')

    html_json = json.loads(html_str)
    return html_json
