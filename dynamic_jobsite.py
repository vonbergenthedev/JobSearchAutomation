from selenium import webdriver


class DynamicJobSite:

    def __init__(self, url, exclusions_list, search_params=None):
        self.url = url
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self.url)
        self.exclusions_list = exclusions_list
        self.search_params = search_params
        self.listings = []

    def get_jobsite_driver(self):
        return self.driver

    def get_listings(self):
        return self.listings

    def set_listing(self, listing):
        self.listings.append(listing)

    def get_exclusions(self):
        return self.exclusions_list

    def print_listings(self):
        for listing in self.listings:
            print(listing.get_job_title())
            print(listing.get_url())
            print(f'Job ID: {listing.get_job_id()}\n')
