# I wanted to automate these tasks:
# 1 - open https://paramgaming.com/?referCode=9BCDF876BC#/signup
# 2 - enter email in input#email field, password in input#password check the checkbox input#disclaimer and click button of type submit 
# 3 - do not close this site on our original tab, head to another tab of https://yopmail.com/en/ in a textbox of input#login enter username and click on a button with title "Check Inbox @yopmail.com"
# 4 - wait for site to load. click on button which has <span class="lmf">noreply@paramlabs.io</span> as its child. wait for 0.2 seconds
# 5 - Copy contents inside the message on screen which is <p style="text-align: center; font-size: 2rem; letter-spacing: 1rem">The_6_digit_otp</p>
# 6 - After getting the otp head to our original tab and enter the otp in the popup input field

# site - https://www.linkedin.com/pulse/preventing-selenium-from-being-detected-soumil-shah
# tried everything from above page, not workm below link works
# imp video - https://www.youtube.com/watch?v=QvaZLa_FKmY
# run - python .\paramFarm.py 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time

# chromeDriverPath = "C:\\Users\\Aditya Bapat\\Downloads\\chrome-win64\\chrome.exe"
# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 

# options._binary_location = chromeDriverPath

# options.add_argument('--no-sandbox')
# options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--incognito")
# # options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--disable-blink-features=AutomationControlled')
# # options.add_experimental_option('useAutomationExtension', False)
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("disable-infobars")


 
# Adding argument to disable the AutomationControlled flag 
# options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
# options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
# options.add_experimental_option("useAutomationExtension", False) 

# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
 
# Setting the driver path and requesting a page 
driver = uc.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#             "source":
#                 "const newProto = navigator.__proto__;"
#                 "delete newProto.webdriver;"
#                 "navigator.__proto__ = newProto;"
#         })

# driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}) 

for i in range(15,17,1):
    username = "paramnoah" + str(i)
    email_domain = "@popol.fr.nf"
    emailId = username + email_domain
    password = "Ramdas*21"

    # Step 1: Open https://paramgaming.com/?referCode=9BCDF876BC#/signup
    paramgaming_url = "https://paramgaming.com/?referCode=9BCDF876BC#/signup"
    driver.get(paramgaming_url)

    time.sleep(5)

    # Step 2: Enter email, password, and check disclaimer
    email_input = driver.find_element(By.ID, "email")
    
    password_input = driver.find_element(By.ID, "password")

    confirm_password_input = driver.find_element(By.ID,"cPassword")

    disclaimer_checkbox = driver.find_element(By.ID, "disclaimer")



    email_input.send_keys(emailId)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    confirm_password_input.send_keys(password)
    time.sleep(2)
    disclaimer_checkbox.click()
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    submit_button.click()
    time.sleep(7)

    # Step 3: Switch to the yopmail tab
    yopmail_url = "https://yopmail.com/en/"
    driver.execute_script(f"window.open('{yopmail_url}', '_blank')")
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])

    # Step 4: Enter username and check inbox
    yopmail_username_input = driver.find_element(By.ID,"login")
    yopmail_username_input.send_keys(username)

    check_inbox_button = driver.find_element(By.XPATH, "//button[@title='Check Inbox @yopmail.com']")
    check_inbox_button.click()

    # Wait for the site to load
    time.sleep(3)  # Adjust this wait time as necessary

    # # Click on the button with noreply@paramlabs.io as its child
    # noreply_button = driver.find_element(By.XPATH, "//button[contains(span, 'noreply@paramlabs.io')]")
    # noreply_button.click()
    # usually first email

    # Wait for 0.2 seconds
    time.sleep(0.5)

    # Step 5: Copy the OTP from the message
    otp_message = driver.find_element(By.CSS_SELECTOR,"p[style='text-align: center; font-size: 2rem; letter-spacing: 1rem']")
    otp = otp_message.text
    print(f"Email: {emailId} otp: {otp}")

    # Step 6: Switch back to the original tab and enter the OTP
    driver.switch_to.window(driver.window_handles[0])
    email_input.send_keys(otp)
    time.sleep(15)




# otp_input = driver.find_element_by_id("otp_input")
# otp_input.send_keys(otp)

# Close the browser
# driver.quit()
