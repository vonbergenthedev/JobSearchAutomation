import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class JobSite:

    def __init__(self, url, exclusions_list):
        self.url = url
        self.html_response = requests.get(self.url)
        # test print for response code
        # print(self.html_response.status_code)

        # sometimes the python requests get is caught by a security feature to try and combat bot usage
        # if alternate code is detected, attempt alternative request structure using urllib request
        if self.html_response.status_code != 200:
            if self.html_response.status_code == 403:
                print('Initial Request Failed [403 Forbidden], trying alternate request...')
                alt_request = Request(
                    url=self.url,
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                self.html_response = urlopen(alt_request).read()
        else:
            self.html_response = self.html_response.text

        self.jobsite_soup = BeautifulSoup(self.html_response, 'html.parser')
        # test print to ensure that the response was converted successfully
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
