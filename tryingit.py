import pygame
from pygame.locals import *


end_of_game_text = font.render("GAME OVER :-(", True, WHITE)
screen.blit(end_of_game_text, [int(SCREEN_WIDTH*.4), int(SCREEN_HEIGHT/2)])
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))