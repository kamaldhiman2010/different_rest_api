import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_using_dj_rest_framework.settings')

app = Celery('api_using_dj_rest_framework')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule ={
    'every-15-seconds':{
        'task':'blogs.tasks.append_data_in_file',
        'schedule':15,
      
    } 
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
