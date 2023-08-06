from monosi.scheduler.handlers.base import BaseResource

class JobsListResource(BaseResource):
    # def _get_jobs(self):
    #     jobs = self.scheduler_manager().get_jobs()
    #     return_json = []
    #     for job in jobs:
    #         return_json.append(self._build_job_dict(job))
    #     return {'jobs': return_json}

    def get(self):
        return {}
        # return self._get_jobs()

class JobsResource(BaseResource):
    def _get_job(self, job_id):
        job = self.scheduler_manager().get_job(job_id)
        if not job:
            return {'error': 'Job not found: %s' % job_id}, 400
        return { 'job': { 'id': job_id } }

    def get_job(self, job_id):
        return self._get_job(job_id)

    # def post(self):
    #     job_id = self.scheduler_manager().add_job(**self.json_args)

    #     # Blocking operation.
    #     self.datastore.add_audit_log(job_id, self.json_args['name'],
    #                                  constants.AUDIT_LOG_ADDED, user=self.username)

    #     response = {
    #         'job_id': job_id}
    #     self.set_status(201)
    #     self.write(response)

    # def _delete_job(self, job_id):
    #     """Deletes a job.
    #     It's a blocking operation.
    #     :param str job_id: String for a job id.
    #     """

    #     job = self._get_job(job_id)

    #     self.scheduler_manager().remove_job(job_id)

    #     self.datastore.add_audit_log(job_id, job['name'], constants.AUDIT_LOG_DELETED,
    #                                  user=self.username, description=json.dumps(job))

    # def delete_job(self, job_id):
    #     """Wrapper for _delete_job() to run on a threaded executor."""
    #     self._delete_job(job_id)