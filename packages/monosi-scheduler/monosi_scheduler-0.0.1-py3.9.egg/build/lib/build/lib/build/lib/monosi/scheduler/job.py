class BaseJob:
    @classmethod
    def run_job(cls, *args, **kwargs):
        job = cls()
        return job.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError('Job not implemented.')
