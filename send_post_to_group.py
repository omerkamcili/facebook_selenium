#!/usr/bin/python3
import os,sys
import random
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

face_username = "username"
face_password = "password"
group_id = "group_id"
url = "share url"


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

time.sleep(random.randrange(1,3))

#click login
loginBtn = driver.find_element(By.XPATH, "//*[@id=\"loginbutton\"]/input")
loginBtn.click()

time.sleep(random.randrange(3,7))

#get group mobile version, because page scrape easier then responsive facebook version
driver.get('https://m.facebook.com/groups/' + group_id)

time.sleep(random.randrange(6,10))

try:
	shareBtn = driver.find_element(By.XPATH, "//*[@id=\"MRoot\"]/div/div[3]/div[1]/table/tbody/tr/td[1]/button")
	shareBtn.click()
	print("click share button")
except WebDriverException:
	print("share button not visiable")
	sql = "UPDATE groups SET status = 0 WHERE id = %d " % (group[0])
	cursor.execute(sql)
	db.commit()
	driver.close()
	sys.exit()

time.sleep(random.randrange(3,10))

try:
	txtArea = driver.find_element(By.XPATH, "//*[@id=\"uniqid_1\"]");
	txtArea.send_keys(url)
	print("enter your url in textarea")
except WebDriverException:
	print("text area not visiable")
	driver.close()
	sys.exit()

time.sleep(random.randrange(3,10))

try:
	sendBtn = driver.find_element(By.XPATH, "//*[@id=\"structured_composer\"]/div[5]/div[1]/div[1]/div[3]/div/button")
	sendBtn.click()
	print("submitted")
	time.sleep(10)
except WebDriverException:
	print("error")
	driver.close()
	sys.exit()

driver.close()