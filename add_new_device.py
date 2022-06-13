from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

primary = "Stock"
site_id = "unknown"

serials = []
assets = []
macs = []


# this assumes the first row of the csv is the column name and
# skips it.
with open('csv_test_g.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			# populates the list of each one
			serials.append(row[0])
			macs.append(row[1])
			assets.append(row[2])
			line_count += 1

	print(serials)
	print(assets)
	print(macs)


def asset_add_device(uname, passw):
	browser = webdriver.Chrome()
	browser.get('https://site.to.request/assets/')
	# search = browser.find_element_by_name('sAMAccountName')
	username = browser.find_element_by_name('uname')
	# password = browser.find_element_by_name('[password]')
	password = browser.find_element_by_name('upass')
	username.send_keys(uname)
	password.send_keys(passw)
	username.send_keys(Keys.RETURN)
	sleep(3)


	for i in range(len(serials)):
		new_serial = serials[i]
		# for macs this is necessary because the scan gun adds an S
		# at the beginning. If the serial is accurate in the csv
		# then comment out this line
		new_serial = new_serial[1:]
	    # Add a device
		new_device = browser.find_element_by_link_text('Add Device').click()
		sleep(1)
		name = browser.find_element_by_id('primaryuser')
		# Input valid user: Stock
		sleep(2)

		name.send_keys(primary)
		name.send_keys(Keys.RETURN)
		# I has now passed AD check.
		# program: None
		program = Select(browser.find_element_by_id('program'))
		program = program.select_by_value('4')
		sleep(1)
		# Asset type: Laptop
		type = Select(browser.find_element_by_id('za1'))
		type = type.select_by_value('3')
		sleep(1)
		# Model: Macbook Air
		model = Select(browser.find_element_by_id('l1m1'))
		model = model.select_by_value('156')
		sleep(1)
		# Site: TECHNOLOGY SERVICES
		site = Select(browser.find_element_by_id('site'))
		site = site.select_by_value('0423')
		sleep(1)
		# Location: unknown
		location = browser.find_element_by_id('location')
		location.send_keys(site_id)
		sleep(1)
		# Account Type: Teacher
		type_of_account = Select(browser.find_element_by_id('accttype'))
		type_of_account = type_of_account.select_by_value('Teacher')
		sleep(1)
		# serial
		serial_number = browser.find_element_by_id('sn')
		serial_number.send_keys(new_serial)
		# asset asset_tags
		asset_tag = browser.find_element_by_id('asset')
		asset_tag.send_keys(assets[i])
		# mac address
		mac_address = browser.find_element_by_id('wla')
		mac_address.send_keys(macs[i])
		sleep(3)
		# Uncomment out the below line when you want to actually save after testing.
		# mac_address.send_keys(Keys.RETURN)
		# sleep(2)
		# browser.find_element_by_css_selector(".submitB[value='Save']").click()
		# sleep(3)

	return browser

# Yeah, this is dumb... but it's meant to be run locally anyhow.
asset_add_device('ADMIN_ACCOUNT', 'PASSWORD')
