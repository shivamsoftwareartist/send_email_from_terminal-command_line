from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

browser = webdriver.Firefox()
browser.get('http://yahoo.com')
sign_in_elem = browser.find_element_by_id('uh-signin')
sign_in_elem.click()


input_name = browser.find_element_by_id('login-username')
name = str(input("Enter your email id: "))
input_name.send_keys(name)
input_name.send_keys(Keys.ENTER)
time.sleep(2)

input_passwd = browser.find_element_by_id('login-passwd')
passwd = getpass.getpass("Insert your password: ")
input_passwd.send_keys(passwd)
input_passwd.send_keys(Keys.ENTER)
time.sleep(3)

mail_button = browser.find_element_by_css_selector("#mega-bottombar-mail > i")
mail_button.click()

compose_mail = browser.find_element_by_partial_link_text("Compose")
compose_mail.click()

#receivermail
reciever_mail = browser.find_element_by_id("message-to-field")
mail_input = str(input("Enter receiver's mail id: "))
reciever_mail.send_keys(mail_input)
reciever_mail.send_keys(Keys.ENTER)

#subject box
subject = browser.find_element_by_css_selector("#mail-app-component > div > div > div.compose-header.en_0 > div:nth-child(3) > div > div > input")
enter_subject = str(input("Enter subject: "))
subject.send_keys(enter_subject)
subject.send_keys(Keys.ENTER)

#textbox
message_box = browser.find_element_by_css_selector("#editor-container > div.rte.em_N.ir_0.o_h.N_6Fd5")
type_message = str(input("Enter your message: ")) 
message_box.send_keys(type_message)


#sendkeys
send_message = browser.find_element_by_css_selector("#mail-app-component > div > div > div.em_N.D_F.ek_BB.p_R.o_h > div:nth-child(2) > div > button")
send_message.click()