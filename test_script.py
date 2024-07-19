from decorators import timer
import time

@timer
def wait_x_seconds(x: int):
    print('script start')
    time.sleep(x)

wait_x_seconds(2)