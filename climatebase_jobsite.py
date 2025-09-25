import json
from jobcard import JobCard


class CBJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        # gather job cards from job search
        job_cards_scripts_dict = json.loads(self.jobsite.get_soup().find_all(name='script')[-1].text)
        job_cards = job_cards_scripts_dict['props']['pageProps']['jobs']

        for entry in job_cards:
            card_excluded = False
            # check if the card title contains a word from the title exclusion bank "remove" if so
            if 'Remote' in entry['remote_preferences']:
                for exclusion in self.jobsite.get_exclusions():
                    if exclusion in entry['title'].lower():
                        card_excluded = True
                        # test print to view exclusions
                        # print(f'\nExclusion found!!!: *{exclusion}*')
                        # print(f'{entry['title']}')
                        break
            else:
                card_excluded = True

            # check if the exclusion tag has been set for job card
            if not card_excluded:
                job_card = JobCard(entry['title'], 'https://climatebase.org/job/' + str(entry['id']))
                self.jobsite.set_listing(job_card)
