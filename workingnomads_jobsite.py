import requests
from bs4 import BeautifulSoup
from jobcard import JobCard


class WNJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        pass
