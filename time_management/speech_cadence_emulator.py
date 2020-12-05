import time


def emulate_speech_cadence(phrase):
    for character in phrase:
        if ord(character) != 32 and ord(character) != 46:
            print(character, end="", flush=True)
            time.sleep(0.05)
        elif ord(character) == 46:
            print(character, end="", flush=True)
            time.sleep(0.5)
        else:
            print(character, end="", flush=True)
            time.sleep(0.16)
