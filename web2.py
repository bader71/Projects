from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Timer

driver = webdriver.Firefox(executable_path=r"C:\Webdriver\geckodriver.exe")
driver.get(#website name)
type_log = driver.find_element_by_xpath('')
type_log.click()
stud = driver.find_element_by_xpath('')
stud.click()
login_user = driver.find_element_by_xpath('')
login_user.send_keys("")
login_pass = driver.find_element_by_xpath('')
login_pass.send_keys("", Keys.ENTER)
def aa():
    academic = driver.find_element_by_xpath('')
    academic.click()

t = Timer(5.0, aa)
t.start()

def ab():
    sp = driver.find_element_by_xpath('')
    sp.click()

i = Timer(10.0, ab)
i.start()
