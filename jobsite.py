import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Jobsite:

    def __init__(self, url, exclusions_list, site_type='static', search_params=None):
        self.url = url

        if site_type == 'static':
            self.headers = {
                'User-Agent': 'Mozilla/5.0'
            }

            self.html_response = requests.get(self.url, headers=self.headers, params=search_params)
            ## Test print for response code
            # print(self.html_response.status_code)
            self.html_response = self.html_response.text

            self.jobsite_soup = BeautifulSoup(self.html_response, 'html.parser')
            ## Test print to ensure that the response was converted successfully
            # print(self.jobsite_soup.prettify())

        if site_type == 'dynamic':
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.url)

        self.exclusions_list = exclusions_list
        self.search_params = search_params
        self.listings = []

    def get_listings(self):
        return self.listings

    def set_listing(self, listing):
        self.listings.append(listing)

    def get_exclusions(self):
        return self.exclusions_list

    def get_jobsite_soup(self):
        return self.jobsite_soup

    def get_jobsite_driver(self):
        return self.driver

    def print_listings(self):
        for listing in self.listings:
            print(f'Job Title: {listing.get_job_title()}')
            print(f'Job URL: {listing.get_url()}')
            print(f'Job ID: {listing.get_job_id()}\n')
