import unittest,selenium,time

from selenium import webdriver

class Test(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.base_url = "https://www.baidu.com"
		
	def tearDown(self):
		self.driver.quit()

	def test_search(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.find_element_by_id("kw").send_keys("python")
		driver.find_element_by_id("su").click()
		time.sleep(3)
		result = driver.execute_script("return document.getElementsByClassName('t c-title-en')[0].innerText")
		self.assertEqual(result,"Welcome to Python.org官网")
		print(result)

if __name__ == '__main__':
	unittest.main()