import pygame
import sys


from config import consts
from src.game_element import GameElement
from src.ship import Ship
from src.meteors import Meteors


if __name__ =="__main__":
    score = 0
    end = False
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(consts.GAME_RES)

    bg = GameElement(consts.BG_BASE_POS, consts.BG_IMG)
    ship = Ship(consts.SH_POS, consts.SH_IMG)
    meteors = Meteors(
        consts.METEOR_BASE_COUNT,
        consts.METEOR_BASE_SPEED,
        consts.METEOR_COUNT_INCREMENT,
        consts.METEOR_SPEED_INCREMENT,
        consts.MET_1_IMG ,
        ship.image.get_size(),
        consts.GAME_RES
    )
    game_font = pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        ship.handle_keys(keys, consts.SH_SPEED, consts.GAME_RES[0])

        bg.draw(window)
        ship.draw(window)

        if end:
            end_text = game_font.render("GAME OVER", True, consts.FONT_COLOR)
            window.blit(end_text, (int(consts.GAME_RES[0]/2) - int(end_text.get_width()/2), int(consts.GAME_RES[1]/2)))
        else:
            score_increment = meteors.move()
            meteors.draw(window)
            end = meteors.check_colision(ship)
       
        meteors.draw(window)

        pygame.display.update()
        clock.tick(consts.GAME_FPS)
