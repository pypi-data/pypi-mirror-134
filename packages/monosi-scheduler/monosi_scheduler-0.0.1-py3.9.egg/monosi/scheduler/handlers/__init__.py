from flask_restful import Api

from monosi.scheduler.handlers.audit_logs import AuditLogsListResource
from monosi.scheduler.handlers.executions import ExecutionsListResource, ExecutionsResource
from monosi.scheduler.handlers.jobs import JobsListResource, JobsResource

api = Api()

api.add_resource(AuditLogsListResource, '/v1/api/logs')

api.add_resource(ExecutionsListResource, '/v1/api/executions')
api.add_resource(ExecutionsResource, '/v1/api/executions/<string:execution_id>')

api.add_resource(JobsListResource, '/v1/api/jobs')
api.add_resource(JobsResource, '/v1/api/jobs/<string:monitor_id>')
