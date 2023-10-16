import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Playlist")
window.geometry("500x400")
window.configure(bg="#191414")

# Create a list to store the selected music files
playlist = []
current_track = 0

# Function to add music files to the playlist
def add_music():
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    for file in files:
        playlist.append(file)
    update_playlist()

# Function to remove a selected track from the playlist
def remove_track():
    if playlist:
        global current_track
        playlist.pop(current_track)
        if current_track >= len(playlist):
            current_track = 0
        update_playlist()

# Function to play the selected music
def play_music():
    if playlist:
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()
        update_pointer()

# Function to pause/resume the currently playing music
def pause_resume_music():
    if pygame.mixer.music.get_busy():
        if pygame.mixer.music.get_paused():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    update_pointer()

# Function to play the next track
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

# Function to play the previous track
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

# Function to update the playlist display
def update_playlist():
    playlist_box.delete(0, tk.END)
    for index, track in enumerate(playlist):
        track_name = os.path.basename(track)
        playlist_box.insert(tk.END, track_name)

# Function to handle track selection from the playlist
def select_track(event):
    selection = playlist_box.curselection()
    if selection:
        global current_track
        current_track = selection[0]
        play_music()

# Function to update the pointer position
def update_pointer():
    playlist_box.itemconfig(current_track, bg="#1DB954")
    playlist_box.itemconfig(current_track-1, bg="#191414")
    playlist_box.itemconfig(current_track+1, bg="#191414")

# Create the playlist frame
playlist_frame = tk.Frame(window, bg="#191414")
playlist_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create the playlist display
playlist_box = tk.Listbox(playlist_frame, selectbackground="#1DB954", selectforeground="white", font=("Arial", 12), bg="#191414", fg="white")
playlist_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add scrollbar to the playlist
playlist_scroll = tk.Scrollbar(playlist_frame)
playlist_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Configure scrollbar
playlist_box.config(yscrollcommand=playlist_scroll.set)
playlist_scroll.config(command=playlist_box.yview)

# Bind the select_track function to the playlist
playlist_box.bind("<<ListboxSelect>>", select_track)

# Create the control frame
control_frame = tk.Frame(window, bg="#191414")
control_frame.pack(pady=10)

# Create the buttons
add_button = tk.Button(control_frame, text="Add Music", command=add_music, font=("Arial", 12), bg="#1DB954", fg="white", padx=10)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(control_frame, text="Remove Track", command=remove_track, font=("Arial", 12), bg="#1DB954", fg="white", padx=10)
remove_button.grid(row=0, column=1, padx=10)

play_button = tk.Button(control_frame, text="Play", command=play_music, font=("Arial", 12), bg="#1DB954", fg="white", padx=20)
play_button.grid(row=1, column=0, padx=10, pady=10)

pause_resume_button = tk.Button(control_frame, text="Pause/Resume", command=pause_resume_music, font=("Arial", 12), bg="#1DB954", fg="white", padx=10)
pause_resume_button.grid(row=1, column=1, padx=10, pady=10)

stop_button = tk.Button(control_frame, text="Stop", command=stop_music, font=("Arial", 12), bg="#1DB954", fg="white", padx=20)
stop_button.grid(row=2, column=0, padx=10, pady=10)

previous_button = tk.Button(control_frame, text="Previous", command=previous_track, font=("Arial", 12), bg="#1DB954", fg="white", padx=10)
previous_button.grid(row=2, column=1, padx=10, pady=10)

next_button = tk.Button(control_frame, text="Next", command=next_track, font=("Arial", 12), bg="#1DB954", fg="white", padx=20)
next_button.grid(row=3, column=0, padx=10, pady=10)

# Configure the track frame to expand with the window size
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Start the main loop
window.mainloop()
