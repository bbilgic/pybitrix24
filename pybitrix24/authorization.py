from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback
from selenium.webdriver.chrome.options import Options
from urllib import parse


class BitrixAuthorization:
    def __init__(self,url,mail,password):
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe',options=chrome_options)
        self.mail = mail
        self.password = password
        self.url = url
        self.code = None
        self.open()
        self.get_code()
        self.driver.close()


    def open(self):
        self.driver.get(self.url)

    def get_code(self):

        try:

            while True:
                try:
                    login_mail =self.driver.find_element_by_xpath('//*[@id="login"]')
                    break
                except:
                    pass

            login_mail.click()
            login_mail.send_keys(self.mail)

            sleep(0.1)
            self.driver.find_element_by_xpath('//button[text()="Next"]').click()


            while True:
                try:
                    password = self.driver.find_element_by_xpath('//*[@id="password"]')
                    break
                except:
                    pass

            password.click()
            password.send_keys(self.password)

            sleep(0.1)
            self.driver.find_element_by_xpath('//button[text()="Next"]').click()

            while True:
                if "127.0.0.1" in self.driver.current_url:
                    break
                
            self.code=parse.parse_qs(parse.urlparse(self.driver.current_url).query)['code'][0]


        except:
            print(traceback.print_exc())
