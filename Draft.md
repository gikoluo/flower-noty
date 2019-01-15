Manual：
https://flower.readthedocs.io/en/latest/index.html

Intro：
https://flower.readthedocs.io/en/latest/screenshots.html


Start the Celery server: 
celery -A noty worker --loglevel=info 

Start the flow server:
celery flower -A noty.tasks --loglevel=info 

* flower -A noty --port=5555 --conf=flowerconfig.py --broker=redis://localhost/
* celery flower -A noty --address=127.0.0.1 --port=5555 --conf=flowerconfig.py


Open the Web admin panel:
http://localhost:5555/broker

Run test message: 
python -m noty.run_tasks 


Test echo Server:
python echo.py



States

READY_STATES
Set of states meaning the task result is ready (has been executed).

UNREADY_STATES
Set of states meaning the task result is not ready (hasn’t been executed).

EXCEPTION_STATES
Set of states meaning the task returned an exception.

PROPAGATE_STATES
Set of exception states that should propagate exceptions to the user.

ALL_STATES
Set of all possible states.


Misc
celery.states.PENDING = u'PENDING'
Task state is unknown (assumed pending since you know the id).

celery.states.RECEIVED = u'RECEIVED'
Task was received by a worker (only used in events).

celery.states.STARTED = u'STARTED'
Task was started by a worker (task_track_started).

celery.states.SUCCESS = u'SUCCESS'
Task succeeded

celery.states.FAILURE = u'FAILURE'
Task failed

celery.states.REVOKED = u'REVOKED'
Task was revoked.

celery.states.RETRY = u'RETRY'
Task is waiting for retry.