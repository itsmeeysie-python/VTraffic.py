from selenium import webdriver 
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class PageTesting(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def wait_rows_in_listtable(self, row_text):                                   
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.1)
		try:
			table = self.browser.find_element_by_id('Table')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except(AssertionError, WebDriverException) as e:
			if time.time()-start_time>cWait:
				raise e

		#table = self.browser.find_element_by_id('Table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Titik Poetry Inc.', self.browser.title)
		hText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', hText)

		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		inName.send_keys('Rufino Delacruz')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Rufino Delacruz')

		time.sleep(.1)
		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		inName.send_keys('Lawrence')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('2: Lawrence')

	def test_other_users_different_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(.1)
		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		inName.send_keys('Lovely Joy')
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Lovely Joy')
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/acey/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lovely Joy', pageBody)
		time.sleep(.1)
		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		inName.send_keys('Eljohn Torres')
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Eljohn Torres')
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, 'acey/.+')
		self.assertNotEqual(viewlist_url, user2_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lovely Joy', pageBody)
		self.assertIn('Eljohn Torres', pageBody)