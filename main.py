import os
from dotenv import load_dotenv
from jobsite import JobSite
from jobsite_exclusions import exclusions_jobtitle_list
from builtin_jobsite import BIJ
from climatebase_jobsite import CBJ
from workingnomads_jobsite import WNJ
from techjobsforgood_jobsite import TJFG

load_dotenv()

# BUILT IN JOBSITE
builtin_jobsite = JobSite(os.environ.get('BUILT_IN_JOBSITE') + os.environ.get('BUILT_IN_SEARCH_TERMS'),
                          exclusions_jobtitle_list)
builtin_jobsite_listings = BIJ(builtin_jobsite)

print(f'\nBuiltin Job Listings:')
for listing in builtin_jobsite_listings.get_listings():
    print(listing.get_job_title())
    print(listing.get_url())

## CLIMATE BASE JOBSITE


## WORKING NOMADS JOBSITE


## TECH JOBS FOR GOOD JOBSITE
