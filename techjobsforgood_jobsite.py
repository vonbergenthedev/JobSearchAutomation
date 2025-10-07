from jobcard import JobCard


class TJFG:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        for temp_card in self.jobsite.get_jobsite_soup().find_all(name='div', class_='ui centered card'):
            temp_card_title = temp_card.div.get('title')
            card_excluded = False

            for exclusion in self.jobsite.get_exclusions():
                if exclusion in temp_card_title.lower():
                    card_excluded = True
                    ## test print to view exclusions
                    # print(f'\nExclusion found!!!: *{exclusion}*')
                    # print(f'{temp_card.div.get('title').strip()}')
                    break

            if not card_excluded:
                job_card = JobCard(temp_card.div.get('title').strip(),
                                   'https://techjobsforgood.com' + temp_card.a.get('href'),
                                   temp_card.a.get('href').rsplit('/', 2)[1])
                self.jobsite.set_listing(job_card)

    def print_jobcard_listings(self):
        self.jobsite.print_listings()
