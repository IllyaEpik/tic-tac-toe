import pygame
import modules.path_to_file as m_path
class Item:
    
    def __init__(self, x = 0, y = 0, width = 180, height = 180):
        self.WIDTH = width
        self.HEGHT = height
        self.X = x
        self.Y = y
        self.CELL = 2
        self.IMG2 = None
    def load_image(self, img, rotate = 0):
        self.IMG = pygame.image.load(m_path.find_file("img/"+img + ".png"))
        self.IMG = pygame.transform.scale(self.IMG, (self.WIDTH, self.HEGHT))
        self.IMG = pygame.transform.rotate(self.IMG, rotate)
        self.IMG2 = img
        
    def blits(self, screen_game):
        screen_game.blit(self.IMG,(self.X, self.Y))