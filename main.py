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

## TODO Add additional sites
## TODO Add additional user

def export_json(jobsite_listings):
    site_export = {}
    site_counter = 0

    for listing in jobsite_listings:
        jobcard_counter = 0
        site_export.update({site_counter: {}})

        for jobcard in listing.get_listings():
            site_export[site_counter][jobcard_counter] = {
                'job_title': jobcard.get_job_title(),
                'job_url': jobcard.get_url(),
                'job_id': jobcard.get_job_id()
            }

            jobcard_counter += 1

        site_counter += 1

    return site_export


load_dotenv()

sites_jobsite_listings = []

## BUILT IN JOBSITE - Static
builtin_jobsite = Jobsite(os.environ.get('BUILT_IN_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                          search_params=search_dict['builtin']['params'], site_type='static')
builtin_jobsite_listings = BIJ(builtin_jobsite)
sites_jobsite_listings.append(builtin_jobsite_listings)

# print(f'\n!!**Builtin Job Listings**!!')
# builtin_jobsite_listings.print_jobcard_listings()

## CLIMATE BASE JOBSITE - Dynamic
climatebase_jobsite = Jobsite(os.environ.get('CLIMATE_BASE_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                              search_params=search_dict['climatebase']['params'], site_type='dynamic')
climatebase_jobsite_listings = CBJ(climatebase_jobsite)
sites_jobsite_listings.append(climatebase_jobsite_listings)

# print(f'\n!!**Climate Base Job Listings**!!')
# climatebase_jobsite_listings.print_jobcard_listings()

## WORKING NOMADS JOBSITE - Dynamic
workingnomads_jobsite = Jobsite(os.environ.get('WORKING_NOMADS_JOBSITE'), exclusions_list=exclusions_jobtitle_list,
                                search_params=search_dict['workingnomads']['params'], site_type='dynamic')
workingnomads_jobsite_listings = WNJ(workingnomads_jobsite)
sites_jobsite_listings.append(workingnomads_jobsite_listings)

# print(f'\n!!**Working Nomads Job Listings**!!')
# workingnomads_jobsite_listings.print_jobcard_listings()

## TECH JOBS FOR GOOD JOBSITE - Static
techjobsforgood_jobsite = Jobsite(os.environ.get('TECH_JOBS_FOR_GOOD_JOBSITE'),
                                  exclusions_list=exclusions_jobtitle_list,
                                  search_params=search_dict['techjobsforgood']['params'], site_type='static')
techjobsforgood_jobsite_listings = TJFG(techjobsforgood_jobsite)
sites_jobsite_listings.append(techjobsforgood_jobsite_listings)

# print(f'\n!!**Tech Jobs for Good Job Listings**!!')
# techjobsforgood_jobsite_listings.print_jobcard_listings()

# TESTING JSON Response
app = Flask(__name__)


@app.route('/')
def index():
    payload = export_json(sites_jobsite_listings)
    response = Response(json.dumps(payload), status=200, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run()
##
