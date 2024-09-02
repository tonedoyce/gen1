import pygame, sys, random
from options import *
from textbox import *

def main():
    screen = pygame.display.set_mode((SCR_WIDE, SCR_HIGH))
    
    drawable = pygame.sprite.Group()
    Textbox.containers = (drawable,)

    textbox = Textbox(0, 200, 400, 100)
    textbox.display = True
    drawable.add(textbox)

    while True:
        for event in pygame.event.get():
		    # input check
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("black", rect=None, special_flags=0)
        print(f"drawable: {drawable}")
        for object in drawable:
            if object.display:
                object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
	main()