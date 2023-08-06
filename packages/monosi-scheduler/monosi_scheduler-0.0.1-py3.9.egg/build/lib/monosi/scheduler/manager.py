from monosi.scheduler.db import db
from monosi.scheduler.handlers import api

class JobManager:
    singleton = None

    def __init__(self, app=None):
        if JobManager.singleton is not None:
            self.app = app
            self.scheduler = MonosiScheduler()
            if app is not None:
                self.init_app(app)
            JobManager.singleton = self
        else:
            return JobManager.singleton

    def init_app(self, app):
        self.scheduler.init_app(app)
        # logging.getLogger('apscheduler.executors.default').setLevel(logging.DEBUG)

        api.init_app(app)
        db.init_app(app)
        db.create_all()

        self.start()

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()

    def add_job(self, job, args=None, trigger='interval', minutes=720, **kwargs):
        self.scheduler.add_scheduler_job(job, args=args, trigger=trigger, minutes=minutes)

    def pause_job(self, job_id):
        self.scheduler.pause_job(job_id)

    def get_job(self, job_id):
        self.scheduler.get_job(job_id)

    def get_jobs(self):
        self.scheduler.get_jobs()

    def remove_job(self, job_id):
        self.scheduler.remove_job(job_id)

    def resume_job(self, job_id):
        self.scheduler.resume_job(job_id)
