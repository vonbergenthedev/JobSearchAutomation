import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

html_response = requests.get(os.environ.get('BUILT_IN_JOBSITE')).text
built_in_jobsite_soup = BeautifulSoup(html_response, "html.parser")

for job_card in built_in_jobsite_soup.find_all(name='a', class_="card-alias-after-overlay"):
    #Only parse if the returned value is headed with /job/ as others are returned in card such as /company/
    if '/job/' in job_card.get('href'):
        #Job Title
        print(f'\n'+job_card.text)
        #Job URL
        print(f'https://builtin.com'+job_card.get('href'))
