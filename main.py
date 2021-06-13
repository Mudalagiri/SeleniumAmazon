import time

import selenium as selenium
from selenium import webdriver

options = []

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element_by_xpath("//input[@name= 'field-keywords']").send_keys("samsung galaxy s20+ mobile phone")
driver.find_element_by_xpath("//input [@value= 'Go']").click()

window_before = driver.window_handles[0]  # to get handle of parent window
window_before_title = driver.title
print(window_before_title)

driver.find_element_by_link_text("Samsung Galaxy S20 + (Cosmic Gray, 8GB RAM, 128GB Storage) Without Offer").click()

window_after = driver.window_handles[1]  # to fetch child widow handle

driver.switch_to.window(window_after)  #switch to child window
time.sleep(2)

window_after_title = driver.title
print(window_after_title)

driver.find_element_by_xpath("//input[@id = 'add-to-cart-button']").click()
time.sleep(2)

driver.switch_to.window(window_before)

driver.execute_script("window.scroll(0, 0);") #scroll to top of the page
driver.refresh()

driver.find_element_by_xpath("//input[@name= 'field-keywords']").clear()  # to clear previous search
driver.find_element_by_xpath("//input[@name= 'field-keywords']").send_keys("The Alchemist")
driver.find_element_by_xpath("//input [@value= 'Go']").click()

# adding new element 'book' to cart

driver.find_element_by_link_text("The Alchemist").click()

window_afterbook = driver.window_handles[2]  # to fetch child widow handle

driver.switch_to.window(window_afterbook)  #switch to child window
time.sleep(2)

window_afterbooktitle = driver.title
print(window_afterbooktitle)

driver.find_element_by_xpath("//input[@id = 'add-to-cart-button']").click()
time.sleep(2)

driver.switch_to.window(window_before)

driver.execute_script("window.scroll(0, 0);")   #scroll to top of the page
driver.refresh()

driver.find_element_by_id("nav-cart-text-container").click()
