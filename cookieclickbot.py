from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

#program tries to click "English" selction for language for 10 seconds
#allows time for chrome to open and for cookie clicker to load 
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    element.click()
    driver.implicitly_wait(8)
    
#If cookie clicker doesn't load after 10 seconds, somethings wrong so .quit()
except:
    driver.quit()
#the cookie you click
bigCookie = driver.find_element_by_id("bigCookie")
#your balance (# of cookies)
num_cookie = driver.find_element_by_id("cookies")
#always preforms the most expensive upgrade my reversing the list of upgrades
#that are able to be bought
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

#creates a simple action change
actions = ActionChains(driver)
actions.double_click(bigCookie)

#how many times to loop thru action change, range is set low for testing but
#can be are large as you want
for i in range(5000):
    #starts action chain
    actions.perform()
    #the "cookies" id is a list and the [0] index is your balance
    count = int(num_cookie.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        #if balance is higher than best upgrade, then purchase
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
