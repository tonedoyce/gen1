import pygame
from options import *

def main():
    print("Welcome to the World of Pokémon")
    screen = pygame.display.set_mode((SCR_WIDE, SCR_HIGH))
    while True:
        for event in pygame.event.get():
			# input check
            if event.type == pygame.QUIT:
            	return
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
	main()