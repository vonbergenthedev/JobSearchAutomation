class JobCard:

    def __init__(self, job_title, url, job_id=None):
        self.job_title = job_title
        self.url = url
        self.job_id = job_id

    def get_job_title(self):
        return self.job_title

    def get_url(self):
        return self.url

    def get_job_id(self):
        return self.job_id
