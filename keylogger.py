import time
import keyboard
from queue import Queue

_KEY_PRESS_DELAY = 0.25

_key_press_queue = Queue()


def listen_for_keypress():
    global _key_press_queue
    while True:
        if keyboard.is_pressed("a"):
            _key_press_queue.put("a")
            time.sleep(_KEY_PRESS_DELAY)
        elif keyboard.is_pressed("b"):
            _key_press_queue.put("b")
            time.sleep(_KEY_PRESS_DELAY)


def dequeue_key_press() -> str:
    return _key_press_queue.get_nowait()


def key_press_is_logged() -> bool:
    return _key_press_queue.qsize() is not 0