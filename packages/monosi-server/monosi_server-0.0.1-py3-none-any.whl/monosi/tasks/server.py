from monosi.server import app
from monosi.tasks.base import TaskBase

class ServerTask(TaskBase):
    def run(self, *args, **kwargs):
        app.run()

