import pygame
import sys
from getkey import getkey, keys
# import os
# import pyglet
# music = pyglet.resource.media('Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3')
# music.play()
pygame.mixer.pre_init(44100)

# initialize it
pygame.mixer.pre_init(44100)
pygame.init()

# configurations
window_height = 600
window_width = 400

# creating window
display = pygame.display.set_mode((window_width, window_height))

pygame.mixer.init()

pygame.mixer.music.load("Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3")
pygame.mixer.music.play(0)

# forever loop
while True:
    key = getkey()
    if key == keys.UP:
        ...  # Handle the UP key
    elif key == keys.DOWN:
        ...  # Handle the DOWN key
    elif key == 'a':
        pygame.mixer.music.pause()  # Handle the `a` key
    elif key == 'Y':
        ...  # Handle `shift-y`
    else:
        # Handle other text characters
        buffer += key
        print(buffer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
