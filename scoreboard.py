import pygame.font
from pygame.sprite import Group
from farmer import Farmer

class Scoreboard:
  def __init__(self, ai_game):
    self.ai_game = ai_game
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats
    self.text_color = (255, 255, 77)
    self.font = pygame.font.SysFont(None, 35)
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_farmers()

  def prep_score(self):
    rounded_score = round(self.stats.score, -1)
    score_str = "Score:"+"{:,}".format(rounded_score)
    self.score_image = self.font.render(score_str, True,
    self.text_color)
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 550
    self.score_rect.top = 20

  def show_score(self):
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.screen.blit(self.level_image, self.level_rect)
    self.farmers.draw(self.screen)




  def check_high_score(self):
     if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()

  def prep_level(self):
      level_str = "Level:"+str(self.stats.level)
      self.level_image = self.font.render(level_str, True, self.text_color)
      self.level_rect = self.level_image.get_rect()
      self.level_rect.right = self.screen_rect.right - 350
      self.level_rect.top = self.score_rect.top

  def prep_high_score(self):
      high_score = round(self.stats.high_score, -1)
      high_score_str = "Record:"+"{:,}".format(high_score)
      self.high_score_image = self.font.render(high_score_str, True, self.text_color)
      self.high_score_rect = self.high_score_image.get_rect()
      self.high_score_rect.right = self.screen_rect.right - 150
      self.high_score_rect.top = self.score_rect.top

  def prep_farmers(self):
    self.farmers = Group()
    for farmer_number in range(self.stats.farmers_left):
      farmer = Farmer(self.ai_game)
      farmer.image = pygame.transform.scale(farmer.image, (100, 52))
      farmer.rect.x = farmer_number * 55
      farmer.rect.y = 10
      self.farmers.add(farmer)