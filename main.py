import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

html_response = requests.get(os.environ.get('BUILT_IN_JOBSITE') + os.environ.get('REMOTE_DEV_JAVASCRIPT_TERMS')).text
built_in_jobsite_soup = BeautifulSoup(html_response, "html.parser")

# ai is very general, gonna have to figure out a way to look around the work maybe for spaces?
# move to separate file after getting working for ease of edit
job_title_exclusions = [
    'manager', 'front-end', 'frontend', 'front end', 'staff', 'principal', 'lead', 'director', 'ai'
]

# gather job cards from job search
for job_card in built_in_jobsite_soup.find_all(name='a', class_="card-alias-after-overlay"):
    card_excluded = False
    # check if the card title contains a word from the title exclusion bank "remove" if so
    for exclusion in job_title_exclusions:
        if exclusion in job_card.text.lower():
            card_excluded = True
            # test print to view exclusions
            print(f'\nExcluding: *{exclusion}*')
            break

    # check if the exclusion tag has been set for each individual job card
    if not card_excluded:
        # Only parse if the returned value is headed with /job/ as others are returned in card such as /company/
        if '/job/' in job_card.get('href'):
            # Job Title
            print(f'\n' + job_card.text)
            # Job URL
            print(f'https://builtin.com' + job_card.get('href'))
    else:
        # test print to view exclusions
        print(f'EXCLUSION: {job_card.text}')
