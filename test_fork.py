import unittest
import time
import selenium
import sys
import argparse
import chromedriver_binary
from selenium.webdriver.common.by import By
from testbase.basepage import BasePageTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.login import Login

# automated test for fork page
class ForkTest(BasePageTestCase):
    url = "https://www.thefork.com/"

    @classmethod
    def setUpClass(self):
        super(ForkTest, self).setUpClass(self)
        self.login = Login(self.browser,self.url)

    # test login by creating new account
    def test_login(self):
        self.login.check_login_page()

    #test personal information by logging into the existing account
    def test_personalinformation(self):
        self.login.check_personalinformation()
        first_name=self.browser.find_element("xpath","//*[@id='USER_SPACE_SECOND_PANEL']/div[2]/section[1]/form/div[2]/div[1]/label/input")
        self.assertEqual("deepthi",first_name.get_attribute('value'))
        last_name=self.browser.find_element("xpath","//*[@id='USER_SPACE_SECOND_PANEL']/div[2]/section[1]/form/div[2]/div[2]/label/input")
        self.assertEqual("cp",first_name.get_attribute('value'))

    @classmethod
    def tearDownClass(self):
        super(ForkTest, self).tearDownClass(self)

if __name__ == "__main__":
    unittest.main(verbosity=2, warnings='ignore')
