# A simple mobile device shopping at eBay without being logged-in, therefore checkout process was omitted

import pytest
import time
import json
import pyautogui
from pywinauto.keyboard import send_keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired capabilities
desired_cap={
  "platformName": "Android",
  "appium:platformVersion": "8.0.0",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.google.android.apps.nexuslauncher",
  "appium:appActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity",
  "appium:automationName": "Appium"
}


def test_flight():
    # create a driver instance
    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)

    # invoke app list
    driver.find_element(By.ID,'com.google.android.apps.nexuslauncher:id/all_apps_handle').click()
    time.sleep(2)

    # launch the app
    driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="eBay"]').click()
    time.sleep(3)

    # click searchbar 1
    driver.find_element(By.ID,'com.ebay.mobile:id/search_box').click()
    time.sleep(2)

    # click serchbar 2
    driver.find_element(By.ID,'com.ebay.mobile:id/search_src_text').send_keys('macbook air m2')
    time.sleep(1)
    driver.execute_script('mobile: performEditorAction', {'action': 'next'})
    time.sleep(3)

    # click the item
    driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="$1,049.00"]').click()
    time.sleep(2)

    # click the quantity list
    driver.find_element(By.ID,'com.ebay.mobile:id/quantity_selection_spinner').click()
    time.sleep(2)

    # choose two items from the drop-down list
    driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]').click()
    time.sleep(2)

    # click 'buy it now' button
    driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Buy It Now"]').click()
    time.sleep(2)

    # Close the browser
    driver.quit()







