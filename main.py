import time
import threading
import keyboard
from queue import Queue

pressed_a = False
pressed_b = False

key_press_queue = Queue()


def main():
    global key_press_queue
    threading.Thread(target=listen_for_keypress).start()
    while True:
        while not key_press_queue.empty():
            print("Pressed key: " + key_press_queue.get_nowait())


def listen_for_keypress():
    global key_press_queue
    while True:
        if keyboard.is_pressed("a"):
            key_press_queue.put("a")
            time.sleep(0.5)
        elif keyboard.is_pressed("b"):
            key_press_queue.put("b")
            time.sleep(0.5)


def bool_to_string(bool_to_convert: bool) -> str:
    return "True" if bool_to_convert else "False"


if __name__ == '__main__':
    print("hello")
    main()
