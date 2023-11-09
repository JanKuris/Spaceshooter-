import pygame
from .game_element import GameElement

# set control 

class Ship(GameElement):
    def handle_keys(self, keys, ship_speed, game_res_x):
        if keys[pygame.K_LEFT] and self.pos[0] > ship_speed: #must be rotation
            self.move((-ship_speed, 0))
        if keys[pygame.K_RIGHT] and self.pos[0] < game_res_x - self.image.get_width(): #must be rotation
            self.move((ship_speed, 0))
        if keys[pygame.K_UP] and self.pos[0] > ship_speed:
            self.move((ship_speed, 0))
        if keys[pygame.K_DOWN] and self.pos[0] < ship_speed:
            self.move((ship_speed, 0))

zmena