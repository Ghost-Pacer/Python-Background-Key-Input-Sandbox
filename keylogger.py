import time
from pynput import keyboard
from queue import Queue

_key_press_queue = Queue()
_should_block_input = False


def listen_for_keypresses():
    with keyboard.Listener(
        on_press=_key_was_pressed, on_release=_key_was_released
    ) as listener:
        listener.join()


def dequeue_key_press() -> str:
    return _key_press_queue.get_nowait()


def key_press_is_logged() -> bool:
    return _key_press_queue.qsize() is not 0


def _key_was_pressed(key):
    global _key_press_queue
    global _should_block_input

    if not _should_block_input:
        if key == keyboard.Key.enter:
            _key_press_queue.put("enter")
        elif key == keyboard.KeyCode.from_char("w"):
            _key_press_queue.put("w")
        elif key == keyboard.KeyCode.from_char("s"):
            _key_press_queue.put("s")
        _should_block_input = True


def _key_was_released(key):
    global _should_block_input
    _should_block_input = False
