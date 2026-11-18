import threading
from playsound3 import playsound

MUSIC_FILE = "8bit_music.mp3"

stop_event = threading.Event()
current_sound = None


def play_music():
    global current_sound

    while not stop_event.is_set():
        current_sound = playsound(MUSIC_FILE, block=False)

        while current_sound.is_alive():
            if stop_event.wait(0.1):
                current_sound.stop()
                return


def start_music():
    stop_event.clear()

    thread = threading.Thread(target=play_music, daemon=True)
    thread.start()


def stop_music():
    stop_event.set()

    if current_sound is not None:
        current_sound.stop()