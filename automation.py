from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()  # maximizes a new chrome browser

#  chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo' in chrome_browser.title)  # True
print('Python Easy Demo' in chrome_browser.title)  # False


assert 'Selenium Easy Demo' in chrome_browser.title
# assert 'Python Easy Demo' in chrome_browser.title  # breaks scripts => string doesn't exist
# assert 'Python Easy Demo' in chrome_browser.body  # breaks scripts => no body tag

show_message_button = chrome_browser.find_element_by_class_name('btn-default')  # grabs button element
print(show_message_button)  # <selenium.webdriver.remote.webelement.WebElement (session="5131eff20d955325062a918bf44243fb", element="40818b6b-c64a-47d3-a389-86babd497477")>
print(show_message_button.get_attribute('innerHTML'))  # Show Message

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')  # gets all the button tags under the get-in form tag
print(user_button)
user_message.clear()
user_message.send_keys('I am extra cool')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I am extra cool' in output_message.text
