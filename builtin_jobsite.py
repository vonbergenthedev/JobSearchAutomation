import requests
from bs4 import BeautifulSoup
from jobcard import JobCard


class BIJ:

    def __init__(self, url, exclusions_list):
        self.url = url
        self.html_response = requests.get(self.url)
        self.soup = BeautifulSoup(self.html_response.text, 'html.parser')
        self.exclusions_list = exclusions_list
        self.listings = []
        self.parse_job_listings()

    def get_listings(self):
        return self.listings

    def parse_job_listings(self):
        # gather job cards from job search
        for job_card in self.soup.find_all(name='a', class_="card-alias-after-overlay"):
            card_excluded = False
            # check if the card title contains a word from the title exclusion bank "remove" if so
            for exclusion in self.exclusions_list:
                if exclusion in job_card.text.lower():
                    card_excluded = True
                    # test print to view exclusions
                    # print(f'\nExcluding: *{exclusion}*')
                    break

            # check if the exclusion tag has been set for each individual job card
            if not card_excluded:
                # Only parse if the returned value is headed with /job/ as others are returned in card such as /company/
                if '/job/' in job_card.get('href'):
                    # print(f'\nCreating Job Card Object:')
                    job_card = JobCard(job_card.text, 'https://builtin.com' + job_card.get('href'))
                    self.listings.append(job_card)
                    # print(f'Object Title: {job_card.get_job_title()}')
                    # print(f'Object URL: {job_card.get_url()}')
