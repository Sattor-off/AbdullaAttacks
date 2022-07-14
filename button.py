import pygame.font
from resource_path import resource_path

class Button:
  def __init__(self, ai_game):

    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.width, self.height = 200, 50
    self.rect = pygame.Rect(0, 0, self.width, self.height)


    self.rect.center = self.screen_rect.center
    self.img = pygame.image.load(resource_path('images/play_button.png'))
    self.img = pygame.transform.scale(self.img, (200, 100))


  def draw_button(self):
    self.screen.blit(self.img, (350,250))