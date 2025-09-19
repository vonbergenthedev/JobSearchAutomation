import os
from dotenv import load_dotenv
from builtin_jobsite import BIJ

load_dotenv()

exclusions_list = [
    'manager', 'front-end', 'frontend', 'front end', 'staff', 'principal', 'lead', 'ai'
]

## BUILT IN JOBSITE
builtin_jobsite_listings = BIJ(os.environ.get('BUILT_IN_JOBSITE') + os.environ.get('REMOTE_DEV_JAVASCRIPT_TERMS'),
                               exclusions_list)

print(f'\nBuiltin Job Listings:')
for listing in builtin_jobsite_listings.get_listings():
    print(listing.get_job_title())
    print(listing.get_url())

## ***** JOBSITE
