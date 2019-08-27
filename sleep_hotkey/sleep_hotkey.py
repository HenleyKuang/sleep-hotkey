import keyboard
import math
import time

DEFAULT_LOOP_INTERVAL = 2
DEFAULT_EXIT_KEY = 'esc'


def sleep(seconds, loop_interval=DEFAULT_LOOP_INTERVAL, exit_key=DEFAULT_EXIT_KEY):
    remaining_seconds = seconds % DEFAULT_LOOP_INTERVAL
    count = math.floor(seconds/loop_interval)
    while not keyboard.is_pressed(exit_key) and count > 0:
        time.sleep(loop_interval)
        count -= 1
    time.sleep(remaining_seconds)
