import os
import requests

from dotenv import load_dotenv

load_dotenv()

BUILT_IN_REMOTE_DEV_JAVASCRIPT_ENDPOINT = os.environ.get('BUILT_IN_REMOTE_DEV_JAVASCRIPT')

response = requests.get(f'{BUILT_IN_REMOTE_DEV_JAVASCRIPT_ENDPOINT}')
job_data_text = response.text


print(job_data_text)


# class BuiltInSiteJobSearch:
#
#     def __init__(self):
#         response = requests.get('BUILT_IN_REMOTE_DEV_JAVASCRIPT_ENDPOINT')
#         self.job_data = response.json()

