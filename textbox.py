import pygame

#creates different textboxes that contain Text
# inherits to game text, menus and prompts
# size to be changed to different subclasses

class Textbox(pygame.sprite.Sprite):
    
    containers = None
    display = False
    
    def __init__(self, x, y, size_x, size_y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x,y)
        self.size = pygame.Vector2(size_x, size_y)
        

    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.position, self.size))
        pygame.draw.rect(surface, "black", (self.position+(5,5), self.size-(10,10)), 5, 5,5,5,5,5)

    def draw_text(self, surface, text):
        pass