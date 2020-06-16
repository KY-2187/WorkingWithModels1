import unittest

from selenium import webdriver

class NewVisitorTest(unittest, TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_and_retrieve_a_list(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do', self.browser.title)

	def test_can_create_new_list(self):
		self.browser.get('http://localhost:8000/tasks')
		input = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			input.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		self.assertIn(
			browser.getCurrentUrl(),
			'http://localhost:8000/task/1'
		)
		self.assertIn(
			'Finish CSCI40 Project',
			self.browser.find_element_by_id('task_name').text
		)
if __name__ == '__main__':
	unittest.main(warnings='ignore')
