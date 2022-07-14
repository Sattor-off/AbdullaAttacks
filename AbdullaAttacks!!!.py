import sys
import os
import pygame
from settings import Settings
from farmer import Farmer
from ketmon import Ketmon
from abdulla import Abdulla
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from resource_path import resource_path


class abdullaInvasion:

 def __init__(self):
   pygame.init()
   pygame.font.init()



   self.settings = Settings()
   self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
   #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
   #self.settings.screen_width = self.screen.get_rect().width
   #self.settings.screen_height = self.screen.get_rect().height
   pygame.display.set_caption("AbdullaAttacks!!!")
   self.bg_color = (self.settings.bg_color)
   self.farmer = Farmer(self)
   self.ketmons = pygame.sprite.Group()
   self.abdullas = pygame.sprite.Group()
   self.stats = GameStats(self)
   self.sb = Scoreboard(self)
   self._create_fleet()
   self.play_button = Button(self)
   self.bg_img = pygame.image.load(resource_path("images/background.png"))
   self.bg_img = pygame.transform.scale(self.bg_img, (900, 600))
   self.programIcon = pygame.image.load(resource_path('images/icon.png'))
   pygame.display.set_icon(self.programIcon)



   my_font = pygame.font.SysFont('Comic Sans MS', 30)
   self.text_surface = my_font.render('By Sattoroff', True, (255, 255, 77))


 def _create_fleet(self):
   abdulla = Abdulla(self)
   abdulla_width, abdulla_height = abdulla.rect.size
   available_space_x = self.settings.screen_width - (2 * abdulla_width)
   number_abdullas_x = available_space_x // (2 * abdulla_width)
   farmer_height = 100
   available_space_y = (self.settings.screen_height -
                        (3 * abdulla_height) - farmer_height)
   number_rows = available_space_y // (2 * abdulla_height)

   for row_number in range(number_rows):
     for abdulla_number in range(number_abdullas_x):
        self._create_abdulla(abdulla_number, row_number)

 def _create_abdulla(self, abdulla_number, row_number):
     abdulla = Abdulla(self)
     abdulla_width, abdulla_height = abdulla.rect.size
     abdulla.x = abdulla_width + 2 * abdulla_width * abdulla_number
     abdulla.rect.x = abdulla.x
     abdulla.rect.y = abdulla.rect.height + 2 * abdulla.rect.height * row_number
     self.abdullas.add(abdulla)

 def _check_fleet_edges(self):
   for abdulla in self.abdullas.sprites():
     if abdulla.check_edges():
        self._change_fleet_direction()
        break

 def _change_fleet_direction(self):
   for abdulla in self.abdullas.sprites():
     abdulla.rect.y += self.settings.fleet_drop_speed
   self.settings.fleet_direction *= -1


 def run_game(self):
   while True:
     self._check_events()

     if self.stats.game_active:
         self.farmer.update()
         self._update_ketmons()
         self._update_abdullas()
     self._update_screen()






 def _check_events(self):
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       sys.exit()
     elif event.type == pygame.KEYDOWN:
       self._check_keydown_events(event)
     elif event.type == pygame.KEYUP:
       self._check_keyup_events(event)
     elif event.type == pygame.MOUSEBUTTONDOWN:
         mouse_pos = pygame.mouse.get_pos()
         self._check_play_button(mouse_pos)

 def _check_play_button(self, mouse_pos):
     button_clicked = self.play_button.rect.collidepoint(mouse_pos)
     if button_clicked and not self.stats.game_active:
       self.settings.initialize_dynamic_settings()
       self.stats.reset_stats()
       self.stats.game_active = True
       self.sb.prep_score()
       self.sb.prep_level()
       self.sb.prep_farmers()
       self.abdullas.empty()
       self.ketmons.empty()
       self._create_fleet()
       self.farmer.center_farmer()
       pygame.mouse.set_visible(False)

 def _check_keydown_events(self,event):
   if event.key == pygame.K_RIGHT:
     self.farmer.moving_right = True
   elif event.key == pygame.K_LEFT:
     self.farmer.moving_left = True
   elif event.key == pygame.K_q:
     sys.exit()
   elif event.key == pygame.K_SPACE:
     self._fire_ketmon()

 def _check_keyup_events(self,event):
   if event.key == pygame.K_RIGHT:
     self.farmer.moving_right = False
   elif event.key == pygame.K_LEFT:
     self.farmer.moving_left = False

 def _fire_ketmon(self):
   if len(self.ketmons) < self.settings.ketmons_allowed:
     new_ketmon = Ketmon(self)
     self.ketmons.add(new_ketmon)


 def _update_screen(self):
   self.screen.fill(self.bg_color)
   self.screen.blit(self.bg_img, (0, 0))
   self.screen.blit(self.text_surface, (0, 550))
   self.farmer.blitme()
   for ketmon in self.ketmons.sprites():
     ketmon.draw_ketmon()


   self.sb.show_score()
   self.abdullas.draw(self.screen)

   if not self.stats.game_active:
       self.play_button.draw_button()

   pygame.display.flip()

 def _update_ketmons(self):
   self.ketmons.update()
   for ketmon in self.ketmons.copy():
     if ketmon.rect.bottom <= 0:
       self.ketmons.remove(ketmon)

   self._check_ketmon_abdulla_collisions()

 def _update_abdullas(self):
   self.abdullas.update()
   self._check_fleet_edges()
   if pygame.sprite.spritecollideany(self.farmer, self.abdullas):
       self._farmer_hit()
   self._check_abdullas_bottom()

 def _check_ketmon_abdulla_collisions(self):
    collisions = pygame.sprite.groupcollide(
    self.ketmons, self.abdullas, True, True)
    if not self.abdullas:
        self.ketmons.empty()
        self._create_fleet()
        self.settings.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()
    if collisions:
        for abdullas in collisions.values():
            self.stats.score += self.settings.abdulla_points * len(abdullas)
        self.sb.prep_score()
        self.sb.check_high_score()

 def _farmer_hit(self):
     if self.stats.farmers_left > 0:
        self.stats.farmers_left -= 1
        self.sb.prep_farmers()
        self.abdullas.empty()
        self.ketmons.empty()
        self._create_fleet()
        self.farmer.center_farmer()
        sleep(0.5)
     else:
         self.stats.game_active = False
         pygame.mouse.set_visible(True)

 def _check_abdullas_bottom(self):
     screen_rect = self.screen.get_rect()
     for abdulla in self.abdullas.sprites():
        if abdulla.rect.bottom >= screen_rect.bottom:
            self._farmer_hit()
            break

if __name__ == '__main__':
  ai = abdullaInvasion()
  ai.run_game()

