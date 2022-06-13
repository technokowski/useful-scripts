from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serials = []
asset_tags = ['20217697', '20220732', '20217994']

def shrek_assets_location(uname, passw):
	browser = webdriver.Chrome()
	browser.get('https://site.to.request/assets/')
	# search = browser.find_element_by_name('sAMAccountName')
	username = browser.find_element_by_name('uname')
	# password = browser.find_element_by_name('[password]')
	password = browser.find_element_by_name('upass')
	username.send_keys(uname)
	password.send_keys(passw)
	username.send_keys(Keys.RETURN)
	sleep(2)
	for i in asset_tags:
		search = browser.find_element_by_link_text('Search').click()
		sleep(2)
		search = Select(browser.find_element_by_id('searchC'))
		sleep(2)
		# search = search.select_by_value('bySN')
		search = search.select_by_value('byAsset')
		sleep(2)
		serial = browser.find_element_by_name('snsearch')
		serial = browser.find_element_by_name('assetsearch')
		sleep(1)
		try:
			serial.send_keys(i)
			serial.send_keys(Keys.RETURN)
			sleep(2)
			browser.find_element_by_css_selector(".submit[value='Edit']").click()
			sleep(2)
			name = browser.find_element_by_id('primaryuser')
			sleep(2)
			name.send_keys(Keys.RETURN)
			sleep(5)
			location = browser.find_element_by_name('location').clear()
			sleep(1)
			location = browser.find_element_by_name('location')
			sleep(1)
			location.send_keys('library')
			sleep(1)
			site = Select(browser.find_element_by_id('site'))
			sleep(1)
			site = site.select_by_value('0133')
			sleep(1)
			location.send_keys(Keys.RETURN)
			sleep(1)
			browser.find_element_by_css_selector(".submitB[value='Save']").click()
			sleep(1)
		except:
			print("No asset tag found")
			print(i)
	search = browser.find_element_by_link_text('Search').click()
	return browser

var = shrek_assets_location('admin', 'password')

def lease(x=0):

	browser = webdriver.Chrome()
	browser.get('https://www.on-site.com/web/signatures/18215691/document?access_key=2.MTqFAQwDQHDlb4ookMcBCACXoenoJoEP814sPlphYJjtdwhmHuwYtqLM0LWHDYbYqpSvd6ArB10GSfIGJCct9uHzU_KDNelkelC4E2e3vPdtgS-nhXLT5cCSAB9LIGm_DrWl9f0Ko7CwKyvNGDYi6YKtm2yCg2waEgNoZF5kVJj3hpFTskRDYlumfk6hD0sX9MtQVPIVjfnXhZtRqv_6Ea5mZcuE9mjEM8KETljjDPVWYvyI1tIP-uLD2z8yyeqJY-0ZuFFCbk3wNFrQ6hzmfc22C74Lw2TF5ABpT1E_Qwg9bQ8D0UGvW_RMlQk0U9S2P2Q4i4g3fOQGAJuI75UdwoAbt6CzemOt6GlTLoeT0PBK0sAOAbBFX7PI2lxQRMtax8sg4ncZcTdg6RG_VzQ5ffDsEeaQzOwmVSeqYsfgZcafLLjmx-4kt2aqKuX3WbTlxErNxlwJHjxHb82ZF2JJn-BezgMgnZ9uRh05NqIKuKKyx152Rmyu0yaGfhZXiFuwsqBxsxy867TF19CG-lcZbD6_wz8sOERUJ5uqA6ConbXTXNS993N4PcG634j4eRQn9MDWQgatAKLcawdObE4aI_uiAyWexZJKHWyBEUu2HnTX8M-KRqqN84WZriDSqhTANQA&present_signer_id[]=24917031#1')

	social = browser.find_element_by_name('ssn4')
	social.send_keys('9012')
	social.send_keys(Keys.RETURN)

	sleep(6)

	for i in range(28,57):
		print(i)
		try:
			# browser.find_element_by_class_name('goto_next_page').click()
			browser.find_element_by_id('thumblink' + str(i)).click()
		except:
			pass

		sleep(7)

		try:
			browser.find_element_by_class_name('initialHL').click()
		except:
			pass

		sleep(5)

		try:
			browser.find_element_by_class_name('signature').click()
		except:
			pass

		sleep(7)
		try:
			browser.find_element_by_class_name('okClickSignature').click()
		except:
			pass
		sleep(7)



	return browser
# var = lease()
