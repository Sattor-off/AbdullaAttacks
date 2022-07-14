import pygame
from pygame.sprite import Sprite
from resource_path import resource_path

class Ketmon(Sprite):

 def __init__(self, ai_game):


     super().__init__()
     self.screen = ai_game.screen
     self.settings = ai_game.settings
     self.color = self.settings.ketmon_color
     self.rect = pygame.Rect(0, 0, self.settings.ketmon_width, self.settings.ketmon_height)
     self.rect.midtop = ai_game.farmer.rect.midtop
     self.y = float(self.rect.y)
     self.ketmon_img = pygame.image.load(resource_path('images/ketmon.png'))
     self.ketmon_img = pygame.transform.scale(self.ketmon_img, (23, 50))

 def update(self):

  self.y -= self.settings.ketmon_speed
  self.rect.y = self.y

 def draw_ketmon(self):

   self.screen.blit(self.ketmon_img, self.rect)