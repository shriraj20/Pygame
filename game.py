import pygame
import sys
from playsound import playsound

# # Input an existing wav filename
# wavFile = input("Enter a wav filename: ")
# # Play the wav file
# playsound(wavFile)
#
# # Input an existing mp3 filename
mp3File = input("Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3")
# Play the mp3 file
playsound(mp3File)

# initialize it
pygame.mixer.pre_init(44100)
pygame.init()

# configurations
window_height = 600
window_width = 400

# creating window
display = pygame.display.set_mode((window_width, window_height))

# forever loop
while True:
    print("hello")
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
