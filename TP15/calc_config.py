from celery import Celery

app = Celery('calc_config', broker='redis://localhost', backend='redis://localhost:6379/0', include=['tasks_calc'])