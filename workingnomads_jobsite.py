from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class WNJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(self.jobsite.url)
        message = driver.find_element(by=By.ID, value='jobs')
        text = message.get_attribute('innerHTML')
        driver.close()

        souped_text = BeautifulSoup(text, 'html.parser')

        # print(souped_text.prettify())

        for entry in souped_text.find_all(name='div', class_='job-desktop'):
            # print(entry.prettify())
            temp_card = entry.find(name='a', class_='open-button ng-binding')

            if temp_card:
                # print(temp_card.prettify())
                print(temp_card.text.strip())
                print(entry.get('id'))
                print(temp_card.get('href'))
            print(
                '--------------------------------------------------------------------------------------------------------')
