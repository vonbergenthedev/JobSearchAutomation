import os
import json
from flask import Flask, Response
from dotenv import load_dotenv
from jobsite import Jobsite
from jobsite_searchterms import search_dict
from jobsite_exclusions import exclusions_jobtitle_list
from builtin_jobsite import BIJ
from climatebase_jobsite import CBJ
from workingnomads_jobsite import WNJ
from techjobsforgood_jobsite import TJFG

site_export = {
    'builtin': {},  # builtin_jobsite_listings,
    'climatebase': {},  # climatebase_jobsite_listings,
    'workingnomads': {},  # workingnomads_jobsite_listings,
    'techjobsforgood': {},  # techjobsforgood_jobsite_listings,
}

load_dotenv()

## BUILT IN JOBSITE - Static
builtin_jobsite = Jobsite(os.environ.get('BUILT_IN_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                          search_params=search_dict['builtin']['params'], site_type='static')
builtin_jobsite_listings = BIJ(builtin_jobsite)

# print(f'\n!!**Builtin Job Listings**!!')
# builtin_jobsite_listings.print_jobcard_listings()

## CLIMATE BASE JOBSITE - Dynamic
climatebase_jobsite = Jobsite(os.environ.get('CLIMATE_BASE_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                              search_params=search_dict['climatebase']['params'], site_type='dynamic')
climatebase_jobsite_listings = CBJ(climatebase_jobsite)

# print(f'\n!!**Climate Base Job Listings**!!')
# climatebase_jobsite_listings.print_jobcard_listings()

## WORKING NOMADS JOBSITE - Dynamic
workingnomads_jobsite = Jobsite(os.environ.get('WORKING_NOMADS_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                                search_params=search_dict['workingnomads']['params'], site_type='dynamic')
workingnomads_jobsite_listings = WNJ(workingnomads_jobsite)

# print(f'\n!!**Working Nomads Job Listings**!!')
# workingnomads_jobsite_listings.print_jobcard_listings()

## TECH JOBS FOR GOOD JOBSITE - Static
techjobsforgood_jobsite = Jobsite(os.environ.get('TECH_JOBS_FOR_GOOD_JOBSITE'),
                                  exclusions_list=exclusions_jobtitle_list,
                                  search_params=search_dict['techjobsforgood']['params'], site_type='static')
techjobsforgood_jobsite_listings = TJFG(techjobsforgood_jobsite)

# print(f'\n!!**Tech Jobs for Good Job Listings**!!')
# techjobsforgood_jobsite_listings.print_jobcard_listings()


## TODO Create function to compress this down, pass in list of listings instead and iterate over.
temp_list = []
counter = 0
for jobcard in builtin_jobsite_listings.get_listings():
    site_export['builtin'][counter] = {'job_title': jobcard.get_job_title(), 'job_url': jobcard.get_url(),
                                       'job_id': jobcard.get_job_id()}
    counter += 1

counter = 0
for jobcard in climatebase_jobsite_listings.get_listings():
    site_export['climatebase'][counter] = {'job_title': jobcard.get_job_title(), 'job_url': jobcard.get_url(),
                                           'job_id': jobcard.get_job_id()}
    counter += 1

counter = 0
for jobcard in workingnomads_jobsite_listings.get_listings():
    site_export['workingnomads'][counter] = {'job_title': jobcard.get_job_title(), 'job_url': jobcard.get_url(),
                                             'job_id': jobcard.get_job_id()}
    counter += 1

counter = 0
for jobcard in techjobsforgood_jobsite_listings.get_listings():
    site_export['techjobsforgood'][counter] = {'job_title': jobcard.get_job_title(), 'job_url': jobcard.get_url(),
                                               'job_id': jobcard.get_job_id()}
    counter += 1

##
# TESTING JSON Response
app = Flask(__name__)


@app.route('/')
def index():
    payload = site_export
    response = Response(json.dumps(payload), status=200, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run()
##

# print("Initial Export")
# print(site_export)
