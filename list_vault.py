from webdrivermanager import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import time

try:
    ChromeDriverManager().download_and_install()
except:
    pass

browser = Chrome()
browser.get('https://www.unrealengine.com/marketplace/en-US/vault')

input("\nPress enter when you're logged in")
print('\n')

try:
    while True:
        time.sleep(2)
        print(*[
            i.text for i in browser.find_elements_by_xpath("//a[contains(@href,'/marketplace/en-US/item/')]") if i.text
        ], sep='\n')
        browser.find_element_by_css_selector("li[class='next']").click()
except NoSuchElementException:
    browser.close()
    exit()
