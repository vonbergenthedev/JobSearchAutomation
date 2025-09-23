import requests
from bs4 import BeautifulSoup
from jobcard import JobCard


class CBJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        print('Parsing job listings')
        print(f'{self.jobsite.get_soup().find('a').prettify()}')


