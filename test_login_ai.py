import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()  
		self.driver.implicitly_wait(10)

	def tearDown(self):
		self.driver.quit()

	def test_valid_login(self):
		driver = self.driver
		driver.get("https://example.com/login")
		driver.find_element(By.ID, "email").send_keys("user@example.com")
		driver.find_element(By.ID, "password").send_keys("correctPassword123")
		driver.find_element(By.ID, "loginBtn").click()
		welcome_msg = driver.find_element(By.CSS_SELECTOR, ".welcome-msg").text
		self.assertEqual(welcome_msg, "Welcome, User")

	def test_invalid_login(self):
		driver = self.driver
		driver.get("https://example.com/login")
		driver.find_element(By.ID, "email").send_keys("user@example.com")
		driver.find_element(By.ID, "password").send_keys("wrongPassword")
		driver.find_element(By.ID, "loginBtn").click()
		error_msg = driver.find_element(By.CSS_SELECTOR, ".error-msg").text
		self.assertEqual(error_msg, "Invalid credentials")

if __name__ == "__main__":
	unittest.main()
