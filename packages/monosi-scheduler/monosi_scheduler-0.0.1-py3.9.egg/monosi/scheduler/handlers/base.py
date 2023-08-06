from flask_restful import Resource

class BaseResource(Resource):
    def scheduler_manager(self):
        from monosi.scheduler.manager import JobManager
        return JobManager.singleton
