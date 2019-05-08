from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://pulse.lnttechservices.com/digite/Request?Key=login')
sleep(5)
elem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
sleep(5)
elem.clear()
elem.send_keys('Python')
sleep(2)
elem.send_keys(Keys.ENTER)