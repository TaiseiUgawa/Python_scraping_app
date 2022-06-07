from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "login form url"
driver.get(url)
time.sleep(3)

#login form click function
companyID=driver.find_element_by_xpath('//*[@id="form_company_id"]')
companyID.clear()
companyID.send_keys("companyID")

userID = driver.find_element_by_xpath('//*[@id="form_login_id"]')    
userID.clear()
userID.send_keys("userID")

password = driver.find_element_by_xpath('//*[@id="form_password"]')     
password.clear()
password.send_keys("password")

login_form = driver.find_element_by_name('commit')
time.sleep(3)
login_form.click()

#attend form click function
mute_form = driver.find_element_by_xpath('/html/body/div[1]/div/section/form/div[1]/div[2]/ul/li[2]')
time.sleep(3)
mute_form.click()

attend_form = driver.find_element_by_xpath('/html/body/div[1]/div/section/form/div[2]/div/div[2]/ul[1]/li[1]/a')
time.sleep(3)
attend_form.click()

driver.implicitly_wait(10)
driver.close()



