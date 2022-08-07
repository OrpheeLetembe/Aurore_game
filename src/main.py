import math

import pygame


from src.game import Game

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Aurore-Aventure")
    screen = pygame.display.set_mode((800, 800))
    background = pygame.image.load("../assets/back.jfif")
    banner = pygame.image.load("../assets/banner.png")
    start_btn = pygame.image.load("../assets/strart.png")
    start_btn_rect = start_btn.get_rect()
    start_btn_rect.x = math.ceil(screen.get_width() / 2.9)
    start_btn_rect.y = math.ceil(screen.get_height() / 2)

    game = Game()

    run_main = True

    while run_main:

        if game.is_playing:
            game.run()
        else:
            screen.blit(background, (0, 0))
            screen.blit(banner, (150, 0))
            screen.blit(start_btn, start_btn_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_main = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_btn_rect.collidepoint(event.pos):
                        game.map_manager.sound.play('click')
                        game.start_game()


