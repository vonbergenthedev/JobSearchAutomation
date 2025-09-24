from jobcard import JobCard


class BIJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        # gather job cards from job search
        for entry in self.jobsite.get_soup().find_all(name='a', class_="card-alias-after-overlay"):
            # test print to view current job card being filtered
            # print(f'\nChecking current job title: {entry.text}')
            # print(entry.get('href'))
            card_excluded = False
            # check if the card title contains a word from the title exclusion bank "remove" if so
            for exclusion in self.jobsite.get_exclusions():
                if exclusion in entry.text.lower():
                    card_excluded = True
                    # test print to view exclusions
                    # print(f'Exclusion found!!!: *{exclusion}*')
                    # print(f'{entry.text}')
                    break

            # check if the exclusion tag has been set for job card
            if not card_excluded:
                # only parse if the returned value is headed with /job/ as others are returned in card such as /company/
                if '/job/' in entry.get('href'):
                    job_card = JobCard(entry.text, 'https://builtin.com' + entry.get('href'))
                    self.jobsite.set_listing(job_card)
