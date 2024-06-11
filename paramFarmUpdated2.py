# I wanted to automate these tasks:
# 1 - open https://paramgaming.com/?referCode=9BCDF876BC#/signup
# 2 - enter email in input#email field, password in input#password check the checkbox input#disclaimer and click button of type submit 
# 3 - do not close this site on our original tab, head to another tab of https://yopmail.com/en/ in a textbox of input#login enter username and click on a button with title "Check Inbox @yopmail.com"
# 4 - wait for site to load. click on button which has <span class="lmf">noreply@paramlabs.io</span> as its child. wait for 0.2 seconds
# 5 - Copy contents inside the message on screen which is <p style="text-align: center; font-size: 2rem; letter-spacing: 1rem">The_6_digit_otp</p>
# 6 - After getting the otp head to our original tab and enter the otp in the popup input field

# site - https://www.linkedin.com/pulse/preventing-selenium-from-being-detected-soumil-shah
# tried everything from above page, did not work, even changed exe binary, provided below link works!
# imp video - https://www.youtube.com/watch?v=QvaZLa_FKmY
# run - python .\paramFarm2.py 

# for saving cookies
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import time

if __name__ == '__main__':

    ua = UserAgent()

    paramgaming_url = "https://paramgaming.com/?referCode=9BCDF876BC#/signup"

    yopmail_url = "https://yopmail.com/en/"

    yopmail_url_cookie = "https://yopmail.com/en/wm"

    # @popol.fr.nf
    email_domain = "@contact.biz.st"

    password = "Ramdas*21"

    captchaKeyValue = '09AM6hZhZNbC3gjTyiGuvDY1TFlcgEoAxtkefshnvA7u9Uyaih9ielLcLKPDDsWbQIQPIQOV44hAkQBJgTypqTnKsjuaRp7V8c0PLkeg'


    for i in range(206,300,1):
        options = webdriver.ChromeOptions() 

        options.add_argument(f'--user-agent={ua.random}')

        # using random user agents
        driver = uc.Chrome(options=options) 

        username = "paramnoah" + str(i)
        emailId = username + email_domain
        
        # This is first tab

        driver.get(paramgaming_url)
        time.sleep(2)

        email_input = driver.find_element(By.ID, "email")
        
        password_input = driver.find_element(By.ID, "password")

        confirm_password_input = driver.find_element(By.ID,"cPassword")

        disclaimer_checkbox = driver.find_element(By.ID, "disclaimer")

        email_input.send_keys(emailId)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        disclaimer_checkbox.click()
        time.sleep(1)

        # submit form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        time.sleep(1)

        # # Second tab - Yopmail
        driver.switch_to.new_window()
        driver.get(yopmail_url)

        if os.path.isfile("yop_cookies.pkl"):
            yop_cookies = pickle.load(open("yop_cookies.pkl", "rb"))
            for cookie in yop_cookies:
                driver.add_cookie(cookie)

        # # enter username
        # yopmail_username_input = driver.find_element(By.ID,"login")
        # yopmail_username_input.send_keys(username)
        # check_inbox_button = driver.find_element(By.XPATH, "//button[@title='Check Inbox @yopmail.com']")
        # check_inbox_button.click()

        defaultKey = True
        captchakeyValue2 = driver.execute_script("return window.localStorage.getItem('_grecaptcha');")
        print("cptch:" + str(driver.execute_script("return window.localStorage.getItem('_grecaptcha');")))
        if captchakeyValue2 is not None:
            print("captchakey is:"  + captchakeyValue2)
            captchaKeyValue = captchakeyValue2
            driver.execute_script("window.localStorage.setItem('_grecaptcha', arguments[0]);", captchakeyValue2)
            defaultKey = False
        else:
            print("def captchakey is:" + captchaKeyValue)
            defaultKey = True
            driver.execute_script("window.localStorage.setItem('_grecaptcha', arguments[0]);", captchaKeyValue)

        driver.add_cookie({'name': 'ywm','value': username})

        driver.get(yopmail_url_cookie)

        pickle.dump(driver.get_cookies(), open("yop_cookies.pkl", "wb"))


        # Wait for the site to load
        if defaultKey:
            time.sleep(36)  # Adjust this wait time as necessary
        else:
            time.sleep(15)
        # trick - yop has more than 1 iframes (imp)
        # Wait for the iframe to be available
        iframe = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.NAME, "ifmail")))

        # Switch to the iframe
        driver.switch_to.frame(iframe)

        # Now you're inside the iframe, locate all <p> tags and extract their text
        p_tags = driver.find_elements(By.TAG_NAME, "p")
        otp = ""
        for p_tag in p_tags:
            if (len(p_tag.text) == 6):
                otp = p_tag.text
                break
            else:
                driver.quit()
                break


        # Switch back to the main frame
        driver.switch_to.default_content()
        driver.delete_all_cookies()
        
        time.sleep(2)
        driver.close()

        print(f"Email: {emailId} otp: {''.join(otp)}")

        # Step 6: Switch back to the original tab and enter the OTP
        # return to first tab
        driver.switch_to.window(driver.window_handles[0])
        otp_input_element = driver.find_element(By.XPATH, "//input[@autocomplete='off' and @aria-label='Please enter OTP character 1']")
        time.sleep(1)
        otp_input_element.send_keys(otp)

        time.sleep(10)
        driver.quit()

    # Close the browser
    driver.quit()
