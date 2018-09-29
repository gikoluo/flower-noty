from celery import Celery

app = Celery('noty',
             broker='amqp://guest:guest@localhost:5672//',
             backend='rpc://',
             include=['noty.tasks'])