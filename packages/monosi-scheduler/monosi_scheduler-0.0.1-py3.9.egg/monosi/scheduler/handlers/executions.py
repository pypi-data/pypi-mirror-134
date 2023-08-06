from monosi.scheduler.handlers.base import BaseResource
from monosi.scheduler.models.execution import Execution

class ExecutionsListResource(BaseResource):
    def _get_executions(self):
        executions = Execution.all()
        return executions

    def get(self):
        return self._get_executions()

class ExecutionsResource(BaseResource):
    def _get_execution(self, execution_id):
        execution = Execution.get_by_id(execution_id)
        if not execution:
            return {'error': 'Execution not found: %s' % execution_id}, 400
        return execution

    def get(self, execution_id):
        return self._get_execution(execution_id)

    def _run_job(self, job_id):
        manager = self.scheduler_manager()
        job = manager.get_job(job_id)
        if not job:
            return {'error': 'Job not found: %s' % job_id}, 400

        job_name = job.args[0]
        execution_id = manager.run_job(job_name, job_id)

        # Audit log
        audit_log = AuditLog(
        	job_id=job_id,
        	# event=constants.AUDIT_LOG_CUSTOM_RUN,
        	description=execution_id,
        	user=self.username()
        )
        audit_log.create()

        return { 'execution_id': execution_id }

    def post(self, job_id):
        self._run_job(job_id)
