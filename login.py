#!/usr/bin/python3
import os,sys
import random
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

face_username = "facebook_username"
face_password = "facebook_password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.set_window_size(1280, 1000)
driver.get('https://www.facebook.com')

#enter username
email = driver.find_element_by_id("email")
email.send_keys(face_username)

#enter password
password = driver.find_element_by_id("pass")
password.send_keys(face_password)

#login
loginBtn = driver.find_element(By.XPATH, "//*[@id=\"loginbutton\"]/input")
loginBtn.click()

# using this line for closing chrome driver
#driver.close()