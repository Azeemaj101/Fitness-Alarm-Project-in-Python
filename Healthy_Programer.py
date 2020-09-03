#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio


from time import time, strftime
from datetime import datetime
import pygame as sound


def Music_Decider(file, Stopper):
    sound.mixer.init()
    sound.mixer.music.load(file)
    sound.mixer.music.set_volume(0.7)
    sound.mixer.music.play()
    while True:
        _user = input()
        if _user == Stopper:
            sound.mixer.music.stop()
            break


def log(mes):
    with open("Fitness_Log.txt", "a") as cout:
        cout.write(f"{mes} : Time: {datetime.now()}:\n")


def IsOfficeTime(currenttime):
    if '12:00:00' < currenttime < '24:00:01':
        return True
    else:
        return False


if __name__ == '__main__':
    # initial Time when program Run
    initial_Water = time()
    initial_Eyes = time()
    initial_Physical = time()

    currenttime = strftime("%H:%M:%S")

    # Set Time
    water_sec = 10
    Eye_sec = 20 * 60
    Physical_sec = 30 * 60

    # while_Loop Till 12 - 11
    while IsOfficeTime(currenttime):
        if time() - initial_Water > water_sec:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            Music_Decider("water.mp3", "drank")
            log("Water")
            initial_Water = time()

        if time() - initial_Eyes > Eye_sec:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            Music_Decider("eyes.mp3", "doneeyes")
            log("Eye")
            initial_Eyes = time()

        if time() - initial_Physical > Physical_sec:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            Music_Decider("physical.mp3", "donephy")
            log("Physical")
            initial_Physical = time()
