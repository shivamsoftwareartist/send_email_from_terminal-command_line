from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass


browser = webdriver.Firefox()
browser.get('http://yahoo.com')
sign_in_elem = browser.find_element_by_id('uh-signin')
sign_in_elem.click()


input_name = browser.find_element_by_id('login-username')
name = str(input("Enter your email id: "))
input_name.send_keys(name)
input_name.send_keys(Keys.ENTER)

input_passwd = browser.find_element_by_id('login-passwd')
passwd = getpass.getpass("Insert your password: ")
input_passwd.send_keys(passwd)
input_passwd.send_keys(Keys.ENTER)
