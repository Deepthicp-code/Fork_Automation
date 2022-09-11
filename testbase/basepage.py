"""Basepage."""
import unittest
import time
import os
import sys
import selenium
import argparse
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePageTestCase(unittest.TestCase):
    def setUpClass(self):
        # set up and configure the chrome webdriver and open up browser
        self.br = os.environ['BROWSER']
        if(self.br.lower() == 'chrome'):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            #chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(options=chrome_options)
            self.browser.maximize_window()
        elif(self.br.lower() == 'firefox'):
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--incognito")
            firefox_options.add_argument("--headless")
            self.browser = webdriver.Firefox(options=firefox_options)
            self.browser.maximize_window()
        else:
            print('Unexpected browser value: ', self.br)
            sys.exit(1)

        # quit the browser after every test case
    def tearDownClass(self):
        self.browser.quit()
