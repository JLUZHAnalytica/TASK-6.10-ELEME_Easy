import shop_info_spider
import shop_list_spider
import parse_result

if __name__ == '__main__':
    web = shop_list_spider.login()
    shop_list_spider.choose(web)
    shopList = shop_list_spider.get_shop_lsit(web)
    shopInfo = shop_info_spider.get_shop_detail(shopList, web.get_cookies())
    parse_result.pares(shopInfo, "output/res/shop_info.json")
