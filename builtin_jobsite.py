from jobcard import JobCard


class BIJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        ## Gather job cards from job search
        for temp_card in self.jobsite.get_soup().find_all(name='a', class_="card-alias-after-overlay"):
            ## Test print to view current job card being filtered
            # print(f'\nChecking current job title: {entry}')
            # print(entry.get('href'))
            # print(entry.get('data-builtin-track-job-id'))
            card_excluded = False
            ## Check if the card title contains a word from the title exclusion bank "remove" if so
            for exclusion in self.jobsite.get_exclusions():
                if exclusion in temp_card.text.lower():
                    card_excluded = True
                    ## Test print to view exclusions
                    # print(f'Exclusion found!!!: *{exclusion}*')
                    # print(f'{entry.text}')
                    break

            ## Check if the exclusion tag has been set for job card
            if not card_excluded:
                ## Only parse if the returned value is headed with /job/ as others are returned in card such as /company/
                if '/job/' in temp_card.get('href'):
                    job_card = JobCard(temp_card.text, 'https://builtin.com' + temp_card.get('href'),
                                       temp_card.get('data-builtin-track-job-id'))
                    self.jobsite.set_listing(job_card)
