from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver_path = r'C:\Users\Aurélien\Desktop\thales_bot\driver\chromedriver.exe'

url = 'https://careers.thalesgroup.com/fr/fr/apply?jobSeqNo=TGPTGWGLOBALR0247718EXTERNALFRFR&source=WORKDAY&step=1'

first_name = 'Kevin'
last_name = 'Geoper'
email = 'gpkevin@gmail.com'
address = 'Rue de la Folie'
experience = "2 years as a software engineer"

print('Initializing webdriver...')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

field = {
    '//*[@id="cntryFields.firstName"]': first_name,
    '//*[@id="cntryFields.lastName"]': last_name,
    '//*[@id="email"]': email,
    '//*[@id="cntryFields.addressLine1"]': address,
    '//*[@id="cntryFields.postalCode"]': '95100',
    '//*[@id="phoneWidget.phoneNumber"]': '',
    '//*[@id="sourceType"]/option[2]': None,
    '//*[@id="cntryFields.regionReference"]/option[101]': None,
    '//*[@id="cntryFields.cityReference"]/option[50]': None,
    '//*[@id="deviceType"]/option[3]': None,
    '//*[@id="privacyCheckBox"]': None,
    '//*[@id="next"]': None
}

try:
    driver.get(url)

    time.sleep(2)

    cookies = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/div/div/div[2]/button[2]'))
    cookies.click()  

    for k, v in field.items():
        if 'option' in k:
            time.sleep(2)

        element = driver.find_element(By.XPATH, k)

        if v == None:
            element.click()
            continue

        element.send_keys(v)

    # if element:
    #     print(type(element))
except Exception as e:
    print(str(e))