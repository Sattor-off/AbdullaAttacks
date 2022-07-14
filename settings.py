class Settings:
 def __init__(self):
   self.screen_width = 900
   self.screen_height = 600
   self.bg_color = (230, 230, 230)
   self.farmer_speed = 1.5
   self.ketmon_speed = 1
   self.ketmon_width = 3
   self.ketmon_height = 15
   self.ketmon_color = (60, 60, 60)
   self.ketmons_allowed = 3
   self.abdulla_speed = 0.1
   self.fleet_drop_speed = 10
   self.fleet_direction = 1
   self.farmer_limit = 3

   self.speedup_scale = 2
   self.score_scale = 1.5
   self.initialize_dynamic_settings()

 def initialize_dynamic_settings(self):
   self.farmer_speed = 1.5
   self.ketmon_speed = 0.5
   self.abdulla_speed = 0.5
   self.fleet_direction = 1
   self.abdulla_points = 50

 def increase_speed(self):
   self.farmer_speed *= self.speedup_scale
   self.ketmon_speed *= self.speedup_scale
   self.abdulla_speed *= self.speedup_scale
   self.abdulla_points = int(self.abdulla_points * self.score_scale)