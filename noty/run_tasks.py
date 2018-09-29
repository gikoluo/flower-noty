from .tasks import longtime_add, remote_notify
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    time.sleep(1)
    r = result.get(timeout=1)
    print('Task result: ', r)


    result = remote_notify.delay("http://127.0.0.1:9000/foo2")
    # at this time, our task is not finished, so it will return False
    print('Task finished? ', result.ready())

    r = result.get(timeout=5)

    print('Task result: ', r)
    # # sleep 10 seconds to ensure the task has been finished
    # time.sleep(10)
    # # now the task should be finished and ready method will return True
    # print('Task finished? ', result.ready())
    # r = result.get(timeout=1)
    # print('Task result: ', r)