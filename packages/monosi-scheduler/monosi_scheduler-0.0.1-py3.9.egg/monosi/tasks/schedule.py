from monosi.config.configuration import Configuration
from monosi.scheduler.job import MonitorJob
from monosi.scheduler.manager import JobManager
from monosi.tasks.base import MonitorsTask

class ScheduleMonitorsTask(MonitorsTask):
    def __init__(self, args, config, manager: JobManager):
        super().__init__(args, config)
        self.manager = manager

    def _process_tasks(self):
        for task in self.task_queue:
            job = MonitorJob(task)
            schedule_minutes = task.monitor.schedule.minutes
            self.manager.add_job(job, self.args, minutes=schedule_minutes)

    @classmethod
    def from_args(cls, args, scheduler):
        try:
            config = Configuration.from_args(args)
        except:
            raise Exception("There was an issue creating the task from args.")

        return cls(args, config, scheduler)

