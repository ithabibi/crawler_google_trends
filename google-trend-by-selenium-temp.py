import requests
from bs4 import BeautifulSoup
import IPython
import IPython.display

import time
import re

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Use Options() instead of ChromeOptions()
options = Options()

options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

###################### set Organic Browser#######################
# # Performance and resource optimization
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-software-rasterizer')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-background-networking')
# options.add_argument('--disable-cache')
# options.add_argument('--disable-webgl')
# options.add_argument('--disable-renderer-backgrounding')
# options.add_argument('--disable-backgrounding-occluded-windows')
# options.add_argument('--disable-extensions')

# # Security and anti-bot measures
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument('--disable-webrtc')
# options.add_argument('--disable-webrtc-ip-handling')
# options.add_argument('--disable-permissions-api')
# options.add_argument('--allow-insecure-localhost')
# options.add_argument('--disable-site-isolation-trials')
# options.add_argument('--disable-blink-features=AutomationControlled')

# # Privacy and annoyance reduction
# options.add_argument('--incognito')
# options.add_argument('--no-default-browser-check')
# options.add_argument('--no-first-run')
# options.add_argument('--disable-notifications')
# options.add_argument('--disable-translate')
# options.add_argument('--mute-audio')
# options.add_argument('--hide-scrollbars')
# options.add_argument('--blink-settings=imagesEnabled=false')

# # Test automation optimizations and debugging
# options.add_argument('--disable-popup-blocking')
# options.add_argument('--disable-print-preview')
# options.add_argument('--disable-pdf-viewer')
# options.add_argument('--disable-url-fetcher')
# options.add_argument('--disable-navigation-preload')
# options.add_argument('--disable-browser-side-navigation')
# options.add_argument('--disable-logging')
# options.add_argument('--disable-devtools-autosave')
# options.add_argument('--disable-experimental-accessibility')
# options.add_argument('--disable-prompt-on-repost')
# options.add_argument('--disable-password-generation')

# # Advanced and custom configurations
# options.add_argument('--lang=fa-IR')
# options.add_argument('--timezone=Iran/Tehran')
# options.add_argument('--disable-google-api-key')
# options.add_argument('--disable-blink-features=NavigationTimingAPI')
# options.add_argument('--no-zygote')
# options.add_argument('--disable-file-system')
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# driver.maximize_window()

driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
driver.get('https://trends.google.com')
driver.get('https://trends.google.com/trends/explore')

# keyword1 = "همراه اول"  # @param {type:"string"}
# keyword2 = "ایرانسل"  # @param {type:"string"}
keyword1 = "java"  # @param {type:"string"}
keyword2 = "python"  # @param {type:"string"}

start_date = datetime.date(2024, 4, 1)  # @param {type:"string"}
end_date = datetime.date(2024, 6, 1)  # @param {type:"string"}

while start_date < end_date:
    driver.get("https://trends.google.com/trends/explore?date=" + str(start_date) + "%20"+str(start_date + relativedelta(months=1))+"&geo=IR&q=" +
               keyword1 + "," + keyword2 + "&hl=en-US")
    time.sleep(15)
    # cookie_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/span[2]/a[2]")
    # cookie_button.click()
    # try:
    download_button = driver.find_element(
        By.XPATH, "/html/body/div[2]/div[2]/div/md-content/div/div/div[5]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]")
    download_button.click()
    # except Exception as e:
    #    print(f"Error: {e}")

    time.sleep(15)
    # driver.refresh() #refresh browser
    print(str(start_date) + " OK")
    start_date = start_date + relativedelta(months=+1)

print("end task")
