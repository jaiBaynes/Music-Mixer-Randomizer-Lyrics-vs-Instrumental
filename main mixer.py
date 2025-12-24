# Music Player with Instrumental and Lyrical Swap

import pygame
import random
import os
import time

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
song5 = ['His World (Instrumental).mp3','His World -Theme of Sonic The Hedgehog.mp3']
song6 = ['With Me (Instrumental Version) - Sonic and the Black Knight [OST].mp3', 'With Me - Sonic and the Black Knight [OST].mp3']


PLAYLIST.append(song4)
PLAYLIST.append(song5)
PLAYLIST.append(song6)


def select_random_track():
    """Randomly selects a song's instrumental version"""
    song_name = random.choice(PLAYLIST)
    return song_name

def play_next_track():
    """Loads and plays the instrumental version of the currently selected track. track."""
    next_track = select_random_track()
    pygame.mixer.music.load(next_track[0])
    pygame.mixer.music.play()
    print(f"Now playing: {next_track[0]}")
    return next_track

def main_music_player():
    pygame.mixer.init()
    pygame.init()

    pygame.mixer.music.set_endevent(MUSIC_END_EVENT)

    current_track = play_next_track()
    elapsed_time = 0
    swap_occurred = False
    randoSwap = 5 #random.uniform(15, 120)  # Random time to swap
    print(randoSwap)

    running = True
    while running:
        if not swap_occurred:
            elapsed_time = pygame.mixer.music.get_pos() / 1000  # Get elapsed time in seconds    
            print(randoSwap - elapsed_time)            
            if elapsed_time >= randoSwap:
                pygame.mixer.music.load(current_track[1])
                pygame.mixer.music.play(0, elapsed_time)  # Resume from where instrumental left off
                #print(f"Now playing: {current_track[1]}")
                swap_occurred = True   
        
        for event in pygame.event.get():
            if event.type == MUSIC_END_EVENT:
                running = False
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.1)  # Short delay before checking for events
        pygame.time.Clock().tick(10)

    pygame.quit()

if __name__ == '__main__':
    main_music_player()
