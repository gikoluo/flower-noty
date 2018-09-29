from __future__ import absolute_import
from celery.utils.log import get_task_logger
from .celery import app
import requests
import time

logger = get_task_logger(__name__)

@app.task
def longtime_add(x, y):
    logger.info('long time task begins')
    #sleep 5 seconds
    #time.sleep(5)
    logger.info('long time task finished')
    return x + y



#Retry in 5s, 30s, 1min, 5min, 1h, 24h and 48h finally.
NOTIFICATION_COUNTDOWNS = [0, 5, 30, 60, 5*60, 60*60, 3600*24, 3600*48]

@app.task(bind=True, max_retries=3)
def remote_notify(self, remote_url, data={}, timeout=2, expect=None, method='GET', auth=None, countdowns=NOTIFICATION_COUNTDOWNS):
    logger.info('remote notify begins')
    try:
        if method.lower() == 'GET':
            r = requests.get(remote_url, params=data, auth=auth, timeout=timeout, allow_redirects=False)
        else:
            r = requests.post(remote_url, data=data, auth=auth, timeout=timeout, allow_redirects=False)

        logger.info('Notified {0} with data [{1}], result: {2}, {3}'.format(remote_url, data, r.status_code, r.text))
        if r.status_code == 200:
            return 'success' + r.text
        else:
            logger.warn('RETRY {0}'.format(self.request.retries))
            r.raise_for_status()
    except Exception:
        self.retry(countdown= countdowns[self.request.retries])