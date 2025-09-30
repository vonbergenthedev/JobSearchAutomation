from bs4 import BeautifulSoup
from jobcard import JobCard
from selenium.webdriver.common.by import By


class CBJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        jobsite_driver = self.jobsite.get_jobsite_driver()
        script_data = jobsite_driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/main/section[2]/div')
        souped_text = BeautifulSoup(script_data.get_attribute('innerHTML'), 'html.parser')
        jobsite_driver.close()

        for temp_card in souped_text.find_all('a'):
            try:
                temp_card_title = temp_card.div.div.div.h2
            except AttributeError:
                pass
            else:
                ## Print card out for debug
                # print('Jobcard Found:')
                # print(temp_card_title.text)
                # print(temp_card.get('href'))
                # job_id = temp_card.get('href').rsplit('/', 2)[1]
                # print(job_id)
                # print('----------------------------------------------------------------------------------------------')

                card_excluded = False

                for exclusion in self.jobsite.get_exclusions():
                    if exclusion in temp_card_title.text.lower():
                        card_excluded = True
                        ## test print to view exclusions
                        # print(f'\nExclusion found!!!: *{exclusion}*')
                        # print(f'{temp_card_title.text}')
                        break

                if not card_excluded:
                    job_id = temp_card.get('href').rsplit('/', 2)[1]
                    job_card = JobCard(temp_card_title.text, temp_card.get('href'), job_id)
                    self.jobsite.set_listing(job_card)
