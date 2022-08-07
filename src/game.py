import pygame


from player import Player
from src.dialogs import DialogsBox
from src.map import MapManager
from src.sounds import SoundManager


class Game:
    def __init__(self):

        # création de la fenetre du jeu
        self.is_playing = False
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Aurore-Aventure")

        # generer un joueur
        self.player = Player()

        # generer une carte et les dialogues
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogsBox()

        # generer le effets sonore
        self.sound_manager = SoundManager()

    def handle_input(self):
        # determination de la direction en fonction de la touche pressee
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def start_game(self):
        self.is_playing = True
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.map_manager.sound.back_sound('music')
        self.dialog_box = DialogsBox()

    def game_over(self):
        player_health = self.map_manager.check_collisions()
        if player_health is not None and player_health <= 0:
            self.player.lost_life()
            self.player.health = self.player.max_health
        if self.player.number_life == 0:

            self.is_playing = False
            self.player.health = self.player.max_health
            self.sound_manager.play('game_over')

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        self.player.save_location()
        self.handle_input()
        self.update()
        self.map_manager.draw()
        self.player.update_health_bar(self.screen)
        self.dialog_box.render(self.screen)
        self.game_over()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.map_manager.check_npc_collisions(self.dialog_box)

        clock.tick(60)
