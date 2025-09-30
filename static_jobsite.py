import requests
from bs4 import BeautifulSoup


class StaticJobSite:

    def __init__(self, url, exclusions_list, search_params=None):
        self.url = url
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
        self.exclusions_list = exclusions_list
        self.listings = []

    def get_listings(self):
        return self.listings

    def set_listing(self, listing):
        self.listings.append(listing)

    def get_exclusions(self):
        return self.exclusions_list

    def get_soup(self):
        return self.jobsite_soup

    def print_listings(self):
        for listing in self.listings:
            print(listing.get_job_title())
            print(listing.get_url())
            print(f'Job ID: {listing.get_job_id()}\n')
