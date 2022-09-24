import unittest
import time
import os
import sys
import argparse
import selenium
import chromedriver_binary
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def check_login_page(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        acceptcookies=self.browser.find_element("xpath","//*[@id='_evidon-accept-button']")
        self.browser.execute_script("arguments[0].click();", acceptcookies)
        login = self.browser.find_element("xpath","//span[text()='Log in']")
        self.browser.implicitly_wait(5)
        self.browser.execute_script("arguments[0].click();", login)
        email=self.browser.find_element("xpath","//*[@id='identification_email']")
        self.browser.execute_script("arguments[0].click();", email)
        email.send_keys("deepthicp95@gmail.com")
        elem= self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[1]/div/div[3]/form[1]/div[2]/button")
        self.browser.execute_script("arguments[0].click();", elem)
        firstname=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[1]/label/input")
        self.browser.execute_script("arguments[0].click();", firstname)
        firstname.send_keys("deepthi")
        lastname=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[2]/label/input")
        self.browser.execute_script("arguments[0].click();", lastname)
        lastname.send_keys("cp")
        phonenumber=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[3]/fieldset/div/div[2]/label/input")
        self.browser.execute_script("arguments[0].click();", phonenumber)
        phonenumber.send_keys("7254333222")
        password=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[4]/div/label/input")
        self.browser.execute_script("arguments[0].click();", password)
        password.send_keys("Suchith@123")
        self.browser.execute_script("window.scrollTo(0, 1000)")
        elem=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[5]/label/span[1]")
        self.browser.execute_script("arguments[0].click();", elem)
        elem=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/div[2]/div[5]/div/div[2]/div/form/div[7]/button")
        self.browser.execute_script("arguments[0].click();", elem)
        time.sleep(10)

    def check_personalinformation(self):
        self.browser.get(self.url)
        name=self.browser.find_element("xpath","//*[@id='root']/div/header/div/div[3]/button/span[1]")
        self.browser.execute_script("arguments[0].click();", name)
        personalinfo=self.browser.find_element("xpath","//*[@id='USER_SPACE_FIRST_PANEL']/ul/li[2]/div/button")
        self.browser.execute_script("arguments[0].click();", personalinfo)
