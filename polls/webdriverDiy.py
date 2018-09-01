from selenium import webdriver
import json

def webdriverDiySet(url,title):
    driver = webdriver.Chrome("D:\pythonFile\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    thisTtitle = driver.execute_script(title)
    returnJson = {"title":thisTtitle}
    driver.quit
    return json.dumps(returnJson)
