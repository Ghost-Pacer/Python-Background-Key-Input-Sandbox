import threading

import keylogger


def main():
    threading.Thread(target=keylogger.listen_for_keypresses).start()
    while True:
        while keylogger.key_press_is_logged():
            print("Pressed key: " + keylogger.dequeue_key_press().value)


if __name__ == "__main__":
    print("Press w, s, or enter and it will be recorded in a background thread")
    print("and printed out on the main thread.")
    main()