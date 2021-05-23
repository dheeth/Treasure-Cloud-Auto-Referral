from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names
from password_generator import PasswordGenerator
import itertools


# Create new Instance of Chrome
driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito") 

for _ in itertools.repeat(None, 8):
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    # Temp Mail
    browser.get("https://www.minuteinbox.com")

    # Your Refereal Link
    browser.execute_script("window.open('https://app.treasure.cloud/auth/signup?code=MTM5MGFhYjQtYmI4ZS0xMWViLTg5MTUtNTVlZWJmNWMyNDFjOmYwYTE0NjdhLTMyYzEtMTFlYi1iMWI4LTViYTQzMmY1ZjBkMA==');")
    

    browser.switch_to.window(browser.window_handles[0])

    time.sleep(2) 

    copyEmailButton = browser.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.copy.cetc')
    copyEmailButton.click()
    print("Email Copied!")

    browser.switch_to.window(browser.window_handles[1])
    print("Switching to Treasure Cloud!")

    time.sleep(3) 

    pasteEmailButton = browser.find_element_by_css_selector('#mat-input-0')
    pasteEmailButton.send_keys(Keys.CONTROL, 'v')
    print("Email Pasted!")

    time.sleep(0.5) 

    signUpButton = browser.find_element_by_css_selector('#signup-button')
    signUpButton.click()

    print("Signup Clicked!")
    time.sleep(10) 

    browser.switch_to.window(browser.window_handles[0])

    refreshButton = browser.find_element_by_css_selector('body > div:nth-child(2) > div:nth-child(4) > div > a.blockLink.refresh')
    refreshButton.click()

    print("Refresh Clicked!")
    time.sleep(5)

    wpccBtn =  browser.find_element_by_css_selector('a.wpcc-btn')
    wpccBtn.click()
    print("Cookies Clicked")

    verifyEmail = browser.find_element_by_css_selector('tr > td.from')
    verifyEmail.click()

    print("Email Clicked!")
    time.sleep(5) 

    browser.switch_to.frame('iframeMail')
    print("Switched to iFrame!")

    verifyButton = browser.find_element_by_css_selector('#hs_cos_wrapper_module_16158863021462 > table > tbody > tr > td > a')
    verifyButton.click()

    print("Verify Button Clicked!")

    browser.switch_to.default_content()
    print("Switched Back")

    time.sleep(7)
    browser.switch_to.window(browser.window_handles[2])

    nameButton = browser.find_element_by_css_selector('#mat-input-1')
    nameButton.send_keys(names.get_full_name())

    pwo = PasswordGenerator()
    pwo.minlen = 10

    password = pwo.generate()

    passButton = browser.find_element_by_css_selector('#mat-input-2')
    passButton.send_keys(password)

    confirmPassButton = browser.find_element_by_css_selector('#mat-input-3')
    confirmPassButton.send_keys(password)

    print("Waiting for Dismiss Button to Vanish")
    time.sleep(5)

    gotitButton = browser.find_element_by_css_selector('button.ng-tns-c58-0')
    gotitButton.click()
    print("Cookie Notification Clicked")

    continueButton = browser.find_element_by_css_selector('#continue-button')
    continueButton.click()

    time.sleep(30)
    print("Details Submitted!")

    browser.quit()
    time.sleep(5)







