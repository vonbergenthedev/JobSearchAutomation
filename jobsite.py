import requests
from bs4 import BeautifulSoup


class JobSite:

    def __init__(self, url, exclusions_list):
        self.url = url
        self.html_response = requests.get(self.url)
        self.jobsite_soup = BeautifulSoup(self.html_response.text, 'html.parser')
        self.exclusions_list = exclusions_list
        self.listings = []

    def get_listings(self):
        return self.listings

    def get_exclusions(self):
        return self.exclusions_list

    def get_soup(self):
        return self.jobsite_soup
