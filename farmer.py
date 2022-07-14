import pygame
from pygame.sprite import Sprite
from resource_path import resource_path

class Farmer(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load(resource_path('images/farmer.png'))
        self.image = pygame.transform.scale(self.image, (300, 161))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = 460
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right+100:
            self.x += self.settings.farmer_speed
        if self.moving_left and self.rect.left+100 > 0:
            self.x -= self.settings.farmer_speed

        self.rect.x = self.x
        self.rect.y = 460

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_farmer(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)