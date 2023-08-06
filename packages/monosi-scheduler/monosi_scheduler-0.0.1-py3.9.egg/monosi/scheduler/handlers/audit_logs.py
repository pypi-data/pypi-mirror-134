from monosi.scheduler.handlers.base import BaseResource
from monosi.scheduler.models.audit_log import AuditLog

class AuditLogsListResource(BaseResource):
    def _get_logs(self):
        logs = AuditLog.all()
        return logs

    def get(self):
        return self._get_logs()
