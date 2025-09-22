from jobcard import JobCard


class BIJ:

    def __init__(self, jobsite):
        self.jobsite = jobsite
        self.parse_job_listings()

    def get_listings(self):
        return self.jobsite.get_listings()

    def parse_job_listings(self):
        # gather job cards from job search
        for job_card in self.jobsite.get_soup().find_all(name='a', class_="card-alias-after-overlay"):
            # test print to view current job card being filtered
            print(f'\nChecking current job title: {job_card.text}')
            print(job_card.get('href'))
            card_excluded = False
            # check if the card title contains a word from the title exclusion bank "remove" if so
            for exclusion in self.jobsite.get_exclusions():
                if exclusion in job_card.text.lower():
                    card_excluded = True
                    # test print to view exclusions
                    print(f'Exclusion found!!!: *{exclusion}*')
                    print(f'{job_card.text}')
                    break

            # check if the exclusion tag has been set for job card
            if not card_excluded:
                # only parse if the returned value is headed with /job/ as others are returned in card such as /company/
                if '/job/' in job_card.get('href'):
                    job_card = JobCard(job_card.text, 'https://builtin.com' + job_card.get('href'))
                    self.jobsite.get_listings().append(job_card)
                    # test print to check jobcard object creation
                    # print(f'\nCreated Job Card Object:')
                    # print(f'Object Title: {job_card.get_job_title()}')
                    # print(f'Object URL: {job_card.get_url()}')
