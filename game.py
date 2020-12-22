import pygame
import sys

# initialize it
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed()[K_q]:
            print("hello")
