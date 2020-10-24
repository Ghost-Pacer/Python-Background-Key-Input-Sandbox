import time
import asyncio
import threading
import keyboard

pressed_a: bool = False
pressed_b: bool = False


async def main():
    keypress_loop = asyncio.new_event_loop()
    threading.Thread(target=keypress_loop.run_forever).start()
    future = asyncio.run_coroutine_threadsafe(listen_for_keypress(), keypress_loop)

    while True:
        time.sleep(0.5)
        print("main is executing...")
        print("Pressed a: " + bool_to_string(pressed_a))
        print("Pressed b: " + bool_to_string(pressed_b))


async def listen_for_keypress():
    while True:
        if keyboard.is_pressed("a"):
            pressed_a = True
        elif keyboard.is_pressed("b"):
            pressed_b = True


def bool_to_string(bool_to_convert: bool) -> str:
    return "True" if bool_to_convert else "False"


if __name__ == '__main__':
    print("hello")
    asyncio.run(main())
