# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import ImageGrab
import os, time, pyperclip

USING_WIN10  = True
CHINESE_MODE = True

# get clipboard
im = ImageGrab.grabclipboard()
if im == None:
    raise ValueError('Nothing from the clipboard.')
im.save('clipboard.png','PNG')

# get file path
filepath = os.getcwd() + r'\clipboard.png'

# open browser
try:
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
    chrome_options.add_argument('log-level=1')
    browser = webdriver.Chrome(executable_path="D:/Programs/Drivers/chromedriver.exe",
                               options=chrome_options)
    browser.get('https://app.xunjiepdf.com/ocr')
    # choose txt mode
    browser.find_element_by_xpath('/html/body/main/section/div/div[3]/div[1]/a[4]').click()
    # upload png
    upload = browser.find_element_by_name('file')
    upload.send_keys(filepath)  # send_keys
    # get result
    result = ''
    while result == '':
        time.sleep(0.1)
        result = browser.find_element_by_name('txt_pdfcontent').get_attribute('value')
    if CHINESE_MODE:
        result = result.replace(',', '，')
        result = result.replace(':', '：')
    pyperclip.copy(result)
    print('Successfully copied into clipboard.')
    if USING_WIN10:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("OCR with Selenium",
                       "OCR result is successfully copied into your clipboard.",
                        threaded=True)
finally:
    browser.quit()
    if os.path.exists("clipboard.png"):
        os.remove("clipboard.png")
    while toaster.notification_active():
        time.sleep(0.1)
