import time
import threading
import keyboard
from queue import Queue

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
            time.sleep(0.25)
        elif keyboard.is_pressed("b"):
            key_press_queue.put("b")
            time.sleep(0.25)


if __name__ == '__main__':
    print("Press a or b and it will be recorded in a background thread")
    print("and printed out on the main thread.")
    main()
