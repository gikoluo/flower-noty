#BROKER_URL = 'redis://localhost'
broker_url = 'pyamqp://guest:guest@localhost:5672/noty/'
#broker_url = 'redis://localhost:6379/0'

result_backend = 'redis://localhost:6379/0'

# Enable debug logging
logging = 'INFO'

timezone = 'Asia/Shanghai'

#how you’d route a misbehaving task to a dedicated queue:
task_routes = {
    'tasks.add': 'low-priority',
}

#instead of routing it you could rate limit the task instead, so that only 10 tasks of this type can be processed in a minute (10/m):
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}