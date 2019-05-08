from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver  = webdriver.Chrome()

driver.get('https://pulse.lnttechservices.com/digite/Request?Key=login')
sleep(5)
login = driver.find_element(By.XPATH,'//*[@id="loginId"]')
sleep(2)
login.send_keys('20147086')
sleep(2)
pwd = driver.find_element(By.XPATH,'//*[@id="password"]')
sleep(2)
pwd.send_keys('gbP%%3011')
sleep(2)
pwd.send_keys(Keys.ENTER)
sleep(5)
first_click = driver.find_element(By.XPATH,'//*[@id="LOCK_Timesheet"]')
sleep(2)
second_click = driver.find_element(By.XPATH,'//*[@id="LOCK_Time_Tracking"]')
sleep(2)
# second_click.click()

