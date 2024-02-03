import datetime
import time
import os
import pygame
import tkinter as tk

def input_time():
    a = input("ENTER TIME FOR ALARM IN FORMAT (HH:MM) : ")
    a = datetime.datetime.strptime(a, "%H:%M")
    return a

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

 
def check_time(a, sound_file):
    while True:
        curr_time = datetime.datetime.now().time()
        if curr_time >= a.time():
            print("oyee balle balle")
            play_sound(sound_file)
            break
        time.sleep(1)   

if __name__ == "__main__":
    sound_file_path = r'YOUR PATH.mp3' #ENTER YOUR OWN PATH OF FILE 
    alarm_time = input_time()

    check_time(alarm_time, sound_file_path)
pygame.time.wait(5000)
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='ITS TIME!!', width=25, command=r.destroy)
button.pack()
r.mainloop()
