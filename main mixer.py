#To Add:
# Modes, different mode functions so that when the song ends a different mode function is called either to end or pick a new song
# If not in folder try another song. IF retries exists song number then quit

# Music Player with Instrumental and Lyrical Swap

import pygame
import random
import os
import time

# Define key global variables
elapsed_time = 0
current_track = ['His World (Instrumental).mp3','His World -Theme of Sonic The Hedgehog.mp3']
swap_occurred = False
randoSwap = 0  

# Define the custom event type for when music ends
MUSIC_END_EVENT = pygame.USEREVENT + 1

# Define your playlist: each key is the song name, value is a list of file paths
"""
PLAYLIST = {
    'song1': ['Live and Learn (Instrumental) - Sonic Adventure 2 [OST].mp3', 'Live and Learn - Sonic Adventure 2 [OST].mp3'],
    'song2': ['Escape From the City (Instrumental) - Sonic Adventure 2 [OST].mp3', 'Escape From the City (City Escape) - Sonic Adventure 2 [OST].mp3'],
    'song3': ['Can You Feel The Sunshine - Sonic R (Instrumental).mp3','Can You Feel the Sunshine - Sonic R [OST].mp3']
}
"""

PLAYLIST = [['Live and Learn (Instrumental) - Sonic Adventure 2 [OST].mp3', 'Live and Learn - Sonic Adventure 2 [OST].mp3'], ['Escape From the City (Instrumental) - Sonic Adventure 2 [OST].mp3', 'Escape From the City (City Escape) - Sonic Adventure 2 [OST].mp3'], ['Can You Feel The Sunshine - Sonic R (Instrumental).mp3','Can You Feel the Sunshine - Sonic R [OST].mp3']]

song4 = ['All Hail Shadow (Crush 40 Ver.) (Instrumental).mp3','All Hail Shadow -Theme of Shadow The Hedgehog.mp3']
PLAYLIST.append(song4)
song5 = ['His World (Instrumental).mp3','His World -Theme of Sonic The Hedgehog.mp3']
PLAYLIST.append(song5)
song6 = ['With Me (Instrumental Version) - Sonic and the Black Knight [OST].mp3', 'With Me - Sonic and the Black Knight [OST].mp3']
PLAYLIST.append(song6)
song7 = ['Catch Me If You Can (Instrumental).mp3','Catch Me If You Can.mp3']
PLAYLIST.append(song7)
song8 = ["A Ghost's Pumpkin Soup - Pumpkin Hill (Instrumental).mp3", "A Ghost's Pumpkin Soup (Pumpkin Hill) - Sonic Adventure 2 [OST].mp3"]
PLAYLIST.append(song8)
song9 = ["Unknown from M.E. ver.1 (Instrumental).mp3", "Unknown from M.E. ver.1.mp3"]
PLAYLIST.append(song9)

def select_random_track():
    """Randomly selects a song's instrumental version"""
    song_name = random.choice(PLAYLIST)
    return song_name

def play_next_track():
    """Loads and plays the instrumental version of the currently selected track. track."""
    global next_track
    next_track = select_random_track()
    pygame.mixer.music.load(next_track[0])
    pygame.mixer.music.play()
    print(f"Now playing: {next_track[0]}")
    return next_track

def reset():
    minTime = 15
    maxTime = 60
    global current_track
    current_track = play_next_track()
    global elapsed_time
    elapsed_time = 0
    global swap_occurred 
    swap_occurred = False
    global randoSwap
    randoSwap = random.uniform(minTime, maxTime)  # Random time to swap
    print(randoSwap)    

def main_music_player():
    pygame.mixer.init()
    pygame.init()
    
    global elapsed_time
    global current_track
    global swap_occurred
    global randoSwap

    pygame.mixer.music.set_endevent(MUSIC_END_EVENT)
    reset() #selects new Instrumental

    running = True
    while running:
        if swap_occurred == False:
            elapsed_time = pygame.mixer.music.get_pos() / 1000  # Get elapsed time in seconds    
            #print(randoSwap - elapsed_time)            
            if elapsed_time >= randoSwap:
                pygame.mixer.music.load(current_track[1])
                pygame.mixer.music.play(0, elapsed_time)  # Resume from where instrumental left off
                print(f"Now playing: {current_track[1]}")
                swap_occurred = True   
        
        for event in pygame.event.get():
            if event.type == MUSIC_END_EVENT:
                reset()            
                #running = False
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.1)  # Short delay before checking for events
        pygame.time.Clock().tick(10)

    pygame.quit() 
    
if __name__ == '__main__':
    main_music_player()
