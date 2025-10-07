import os
from dotenv import load_dotenv
from jobsite import Jobsite
from jobsite_searchterms import search_dict
from jobsite_exclusions import exclusions_jobtitle_list
from builtin_jobsite import BIJ
from climatebase_jobsite import CBJ
from workingnomads_jobsite import WNJ
from techjobsforgood_jobsite import TJFG

## TODO Create Dictionary/JSON export

load_dotenv()

## BUILT IN JOBSITE - Static
builtin_jobsite = Jobsite(os.environ.get('BUILT_IN_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                          search_params=search_dict['builtin']['params'], site_type='static')
builtin_jobsite_listings = BIJ(builtin_jobsite)

print(f'\n!!**Builtin Job Listings**!!')
builtin_jobsite_listings.print_jobcard_listings()

## CLIMATE BASE JOBSITE - Dynamic
climatebase_jobsite = Jobsite(os.environ.get('CLIMATE_BASE_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                              search_params=search_dict['climatebase']['params'], site_type='dynamic')
climatebase_jobsite_listings = CBJ(climatebase_jobsite)

print(f'\n!!**Climate Base Job Listings**!!')
climatebase_jobsite_listings.print_jobcard_listings()

## WORKING NOMADS JOBSITE - Dynamic
workingnomads_jobsite = Jobsite(os.environ.get('WORKING_NOMADS_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                                search_params=search_dict['workingnomads']['params'], site_type='dynamic')
workingnomads_jobsite_listings = WNJ(workingnomads_jobsite)

print(f'\n!!**Working Nomads Job Listings**!!')
workingnomads_jobsite_listings.print_jobcard_listings()

## TECH JOBS FOR GOOD JOBSITE - Static
techjobsforgood_jobsite = Jobsite(os.environ.get('TECH_JOBS_FOR_GOOD_JOBSITE'),
                                  exclusions_list=exclusions_jobtitle_list,
                                  search_params=search_dict['techjobsforgood']['params'], site_type='static')
techjobsforgood_jobsite_listings = TJFG(techjobsforgood_jobsite)

print(f'\n!!**Tech Jobs for Good Job Listings**!!')
techjobsforgood_jobsite_listings.print_jobcard_listings()
