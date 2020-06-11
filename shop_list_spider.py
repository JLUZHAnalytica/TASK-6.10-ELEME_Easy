def get_shop_lsit(web):
	shop_id = []
	for i in range(5):
		web.execute_script('document.getElementsByClassName("index-container_10L_lQb shop-{}")[0].click()'.format(i))
		shop_id.append(web.current_url.split('id=')[1].split('&')[0])
		web.back()
		i+=1
	return shop_id