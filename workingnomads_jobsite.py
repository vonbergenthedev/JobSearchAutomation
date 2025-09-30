from bs4 import BeautifulSoup
from jobcard import JobCard
from selenium.webdriver.common.by import By


class WNJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        jobsite_driver = self.jobsite.get_jobsite_driver()
        script_data = jobsite_driver.find_element(by=By.ID, value='jobs')
        souped_text = BeautifulSoup(script_data.get_attribute('innerHTML'), 'html.parser')
        jobsite_driver.close()

        for entry in souped_text.find_all(name='div', class_='job-desktop'):
            temp_card = entry.find(name='a', class_='open-button ng-binding')
            card_excluded = False

            if temp_card:
                for exclusion in self.jobsite.get_exclusions():
                    if exclusion in temp_card.text.strip().lower():
                        card_excluded = True
                        ## Test print to view exclusions
                        # print(f'\nExclusion found!!!: *{exclusion}*')
                        # print(f'{temp_card.text.strip()}')
                        break
            else:
                card_excluded = True

            ## Check if the exclusion tag has been set for job card
            if not card_excluded:
                job_id = temp_card.get('href').rsplit('-', 1)[1]

                try:
                    int(job_id)

                ## job_id is a word, the site does not use an int for the tail end of the url
                except ValueError:
                    job_card = JobCard(temp_card.text.strip(), 'https://www.workingnomads.com' + temp_card.get('href'))
                    self.jobsite.set_listing(job_card)

                else:
                    job_card = JobCard(temp_card.text.strip(), 'https://www.workingnomads.com' + temp_card.get('href'),
                                       job_id)
                    self.jobsite.set_listing(job_card)

    def print_jobcard_listings(self):
        self.jobsite.print_listings()
