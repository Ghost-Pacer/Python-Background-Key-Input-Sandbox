import time
import keyboard


def main():
    while True:
        time.sleep(2)
        print("main is executing...")
        listen_for_keypress()


def listen_for_keypress():
    if keyboard.is_pressed("a"):
        print("test")


if __name__ == '__main__':
    print("hello")
    main()
