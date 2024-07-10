import tkinter as tk
from tkinter import messagebox, filedialog
import datetime
import time
import pygame
import threading
import os

# Initialize pygame mixer
pygame.mixer.init()

def set_alarm(alarm_time, alarm_tone, snooze_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("Wake up!")
            pygame.mixer.music.load(alarm_tone)
            pygame.mixer.music.play()
            messagebox.showinfo("Alarm", "Time to wake up!")
            snooze_option = messagebox.askquestion("Alarm", "Do you want to snooze?")
            if snooze_option == 'yes':
                print(f"Snoozing for {snooze_time} seconds...")
                time.sleep(snooze_time)
                snooze_alarm_time = (datetime.datetime.now() + datetime.timedelta(seconds=snooze_time)).strftime("%H:%M:%S")
                alarm_time = snooze_alarm_time
            else:
                print("Alarm stopped.")
                pygame.mixer.music.stop()
                break
        time.sleep(1)

def start_alarm():
    alarm_time = time_entry.get()
    alarm_tone = tone_entry.get()
    snooze_time = int(snooze_entry.get())
    alarm_tone = os.path.normpath(alarm_tone)
    alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, alarm_tone, snooze_time))
    alarm_thread.start()

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Alarm Tone",
                                          filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    tone_entry.delete(0, tk.END)
    tone_entry.insert(0, filename)

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x300")
root.resizable(False, False)

# Set the main window's background color
root.configure(bg='#2E4053')

# Create a frame for the input fields and buttons
frame = tk.Frame(root, bg='#2E4053')
frame.pack(pady=20)

# Create and place the time label and entry
time_label = tk.Label(frame, text="Set Alarm Time (HH:MM:SS):", fg='white', bg='#2E4053', font=("Helvetica", 12))
time_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')
time_entry = tk.Entry(frame, font=("Helvetica", 12), width=15)
time_entry.grid(row=0, column=1, pady=10, padx=10)

# Create and place the tone label and entry with a browse button
tone_label = tk.Label(frame, text="Alarm Tone File Path:", fg='white', bg='#2E4053', font=("Helvetica", 12))
tone_label.grid(row=1, column=0, pady=10, padx=10, sticky='w')
tone_entry = tk.Entry(frame, font=("Helvetica", 12), width=15)
tone_entry.grid(row=1, column=1, pady=10, padx=10)
browse_button = tk.Button(frame, text="Browse", command=browse_file, bg='#1ABC9C', fg='white', font=("Helvetica", 10))
browse_button.grid(row=1, column=2, pady=10, padx=10)

# Create and place the snooze label and entry
snooze_label = tk.Label(frame, text="Snooze Time (seconds):", fg='white', bg='#2E4053', font=("Helvetica", 12))
snooze_label.grid(row=2, column=0, pady=10, padx=10, sticky='w')
snooze_entry = tk.Entry(frame, font=("Helvetica", 12), width=15)
snooze_entry.grid(row=2, column=1, pady=10, padx=10)

# Create and place the set alarm button
set_button = tk.Button(root, text="Set Alarm", command=start_alarm, bg='#1ABC9C', fg='white', font=("Helvetica", 12))
set_button.pack(pady=20)

# Run the GUI main loop
root.mainloop()
