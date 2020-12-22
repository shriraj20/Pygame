import pygame
import sys
# initialize it
pygame.init()

# configurations
window_height = 600
window_width = 400

# creating window
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
display = pygame.display.set_mode((window_width, window_height))

pygame.mixer.init()

pygame.mixer.music.load("Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3")
pygame.mixer.music.play(0)


# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
#         if event.mod == pygame.K_UP:
#             print('No modifier keys were in a pressed state when this '
#                   'event occurred.')

# forever loop

# fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if pygame.key.get_pressed()[pygame.K_f]:
        #     fullscreen = not fullscreen
        #     if fullscreen:
        #         screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
        #     else:
        #         display = pygame.display.set_mode((window_width, window_height))
        if pygame.key.get_pressed()[pygame.K_n]:
            if pygame.mixer.music.load("Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3"):
                pygame.mixer.music.pause()
                pygame.mixer.music.unload("Marshmello x Imanbek (Ft. Usher) - Too Much (Official Music Video).mp3")