import time
import threading
import keyboard

pressed_a = False
pressed_b = False

key_press = ""


def main():
    global key_press
    threading.Thread(target=listen_for_keypress).start()
    while True:
        # print("main is executing...")
        # print("Pressed a: " + bool_to_string(pressed_a))
        # print("Pressed b: " + bool_to_string(pressed_b))
        if key_press is not "":
            print("Pressed key: " + key_press)
            key_press = ""


def listen_for_keypress():
    global key_press
    while True:
        if keyboard.is_pressed("a"):
            key_press = "a"
            time.sleep(0.5)
        elif keyboard.is_pressed("b"):
            key_press = "b"
            time.sleep(0.5)


def bool_to_string(bool_to_convert: bool) -> str:
    return "True" if bool_to_convert else "False"


if __name__ == '__main__':
    print("hello")
    main()
