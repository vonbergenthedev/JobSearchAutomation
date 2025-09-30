import os
from dotenv import load_dotenv
from dynamic_jobsite import DynamicJobSite
from static_jobsite import StaticJobSite
from jobsite_searchterms import search_dict
from jobsite_exclusions import exclusions_jobtitle_list
from builtin_jobsite import BIJ
from climatebase_jobsite import CBJ
from workingnomads_jobsite import WNJ
from techjobsforgood_jobsite import TJFG

## TODO Create Dictionary/JSON export

load_dotenv()

## BUILT IN JOBSITE - Static
builtin_jobsite = StaticJobSite(os.environ.get('BUILT_IN_JOBSITE'), exclusions_jobtitle_list,
                                search_dict['builtin']['params'])
builtin_jobsite_listings = BIJ(builtin_jobsite)

print(f'\n!!**Builtin Job Listings**!!')
builtin_jobsite_listings.print_jobcard_listings()

## CLIMATE BASE JOBSITE - Dynamic
climatebase_jobsite = DynamicJobSite(os.environ.get('CLIMATE_BASE_JOBSITE'), exclusions_jobtitle_list,
                                     search_dict['climatebase']['params'])
climatebase_jobsite_listings = CBJ(climatebase_jobsite)

print(f'\n!!**Climate Base Job Listings**!!')
climatebase_jobsite_listings.print_jobcard_listings()

## WORKING NOMADS JOBSITE - Dynamic
workingnomads_jobsite = DynamicJobSite(os.environ.get('WORKING_NOMADS_JOBSITE'), exclusions_jobtitle_list,
                                       search_dict['workingnomads']['params'])
workingnomads_jobsite_listings = WNJ(workingnomads_jobsite)

print(f'\n!!**Working Nomads Job Listings**!!')
workingnomads_jobsite_listings.print_jobcard_listings()

## TECH JOBS FOR GOOD JOBSITE - Static
techjobsforgood_jobsite = StaticJobSite(os.environ.get('TECH_JOBS_FOR_GOOD_JOBSITE'), exclusions_jobtitle_list,
                                        search_dict['techjobsforgood']['params'])
techjobsforgood_jobsite_listings = TJFG(techjobsforgood_jobsite)

print(f'\n!!**Tech Jobs for Good Job Listings**!!')
techjobsforgood_jobsite_listings.print_jobcard_listings()
