search_dict = {

    'builtin': {
        'params': {
            # 'daysSinceUpdated': '7',
            ## Currently, below terms make it too strict to return entries
            # 'city': 'Billings',+
            # 'state': 'Montana',
            # 'country': 'USA',
            # 'searcharea': '5mi',
            # 'allLocations': 'true',
            # '?page': '1',
        }
    },

    'climatebase': {
        'params': {
            # 'categories': 'Software+%26+IT%3ABack-end+Engineering%2CFull-stack+Engineering%7CSoftware+%26+IT%3ABack-end+Engineering%2CFull-stack+Engineering',
            # 'date': 'last7',
            # 'remote_preferences': 'Remote',
            # 'remote': 'true',
            # 'job_types': 'Full+time+role',
        },
    },

    'workingnomads': {
        'params': {
            # 'location': 'north-america',
            # 'category': 'development',
            # 'positionType': 'full-time',
            # 'salary': '150000',
            # 'postedDate': '7',
            # 'tag': 'software-engineering',
        }
    },
    'techjobsforgood': {
        'params': {
            #     'job_function': 'Software+Engineering',
            #     'locations': 'remote',
            #     'q': 'js',
            ## This level will need additional logic as the call is &seniority=... with the index being the required level
            ## and each respective query added together, as such: '&seniority=Mid+Level&seniority=Senior'
            #     'seniority': {
            #         0: 'Mid+Level',
            #         1: 'Senior'
            #     },
            #     'remote_jobs': 'on',
        }
    }
}
