from dataclasses import dataclass
import pygame
import pytmx
import pyscroll


from src.bonus import Bonus, FireBall, Heart
from src.monters import Monsters, BigMonster
from src.player import NPC
from src.sounds import SoundManager


@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    life: list[pygame.Rect]
    poison: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]
    monsters: list[Monsters]
    bonus: list[Bonus]
    fire_ball: list[FireBall]
    hearts: list[Heart]
    big_monster: list[BigMonster]


class MapManager:
    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = 'world'
        self.sound = SoundManager()

        self.register_map("world", portals=[
            Portal(from_world='world', origin_point='enter_house1', target_world='house1',
                   teleport_point='spawn_house1'),
            Portal(from_world='world', origin_point='enter_house2', target_world='house2',
                   teleport_point='spawn_house2'),
            Portal(from_world='world', origin_point='enter_house3', target_world='house3',
                   teleport_point='spawn_house3'),
            Portal(from_world='world', origin_point='enter_world_lab', target_world='labyrinthe',
                   teleport_point='spawn_world_lab'),
            Portal(from_world='world', origin_point='enter_world_hiver', target_world='hiver',
                   teleport_point='spawn_world_hiver'),
            Portal(from_world='world', origin_point='enter_world_foret', target_world='foret',
                   teleport_point='spawn_world_foret'),


        ], npcs=[
            NPC('paul', nb_points=14, dialog=[
                "Bonjour Aurore, je m’appelle Paul.", " Bienvenue au village de l’Est.",
                "La vie ici était paisible avant,", " mais depuis que Zorac le maléfique a",
                " ouvert un passage entre son château et le village,",
                "il y’a des phénomènes étranges.", " J’espère que tu pourras nous aider."]),
            NPC('robin', nb_points=8, dialog=[
                "Salut Aurore! je suis Robin,", " le roi ma chargé de la surveillance du pont Sud.",
                "Si tu veux te rendre au château de Zorac,", " cherche les cristaux.",
                "Mais soit prudente,", " on raconte que ce maléfique est entouré de monstres.",
                "Bonne chance"
            ]),
            NPC('jean', nb_points=2, dialog=[
               "j'ai mal à la tête"
            ]),




        ]),
        self.register_map("house1", portals=[
            Portal(from_world='house1', origin_point='exit_house1', target_world='world',
                   teleport_point='enter_house1_exit')
        ])

        self.register_map("house2", portals=[
            Portal(from_world='house2', origin_point='exit_house2', target_world='world',
                   teleport_point='enter_house2_exit')
        ])

        self.register_map("house3", portals=[
            Portal(from_world='house3', origin_point='exit_house3', target_world='world',
                   teleport_point='enter_house3_exit')

        ], hearts=[
            Heart("coeur", 337, 241)
        ])

        self.register_map("house4", portals=[
            Portal(from_world='house4', origin_point='enter_house4_hiver', target_world='hiver',
                   teleport_point='spawn_house4_hiver')
        ])

        self.register_map("house5", portals=[
            Portal(from_world='house5', origin_point='enter_house5_hiver', target_world='hiver',
                   teleport_point='spawn_house5_hiver')
        ])

        self.register_map("labyrinthe", portals=[
            Portal(from_world='labyrinthe', origin_point='exit_lab', target_world='donjon',
                   teleport_point='spawn_donjon'),
            Portal(from_world='labyrinthe', origin_point='enter_cave_lab', target_world='cave_lab',
                   teleport_point='spawn_lab_cave'),
            Portal(from_world='labyrinthe', origin_point='enter_lab_world', target_world='world',
                   teleport_point='spawn_lab_world')
        ], monsters=[
            Monsters("boss1", nb_points=2, speed=3, attaque=5),
            Monsters("boss2", nb_points=4, speed=1, attaque=2),
            Monsters("boss3", nb_points=2, speed=2, attaque=2),
            Monsters("boss4", nb_points=15, speed=1, attaque=2),
            Monsters("boss6", nb_points=4, speed=1, attaque=2),

        ], bonus=[
            Bonus("bonus", 704, 223),
            Bonus("bonus", 543, 400),
            Bonus("bonus", 224, 608),
            Bonus("bonus", 48, 543),
            Bonus("bonus", 528, 321),
            Bonus("bonus", 208, 720),
        ])

        self.register_map("cave_lab", portals=[
            Portal(from_world='cave_lab', origin_point='exit_cave_lab', target_world='labyrinthe',
                   teleport_point='spawn_cave_lab')

        ], bonus=[
            Bonus("bonus", 320, 31),
            Bonus("bonus", 352, 32),
            Bonus("bonus", 335, 64),
            Bonus("bonus", 320, 144),
            Bonus("bonus", 251, 144),
            Bonus("bonus", 208, 144),
            Bonus("bonus", 208, 64),
            Bonus("bonus", 208, 32),
            Bonus("bonus", 48, 33),
            Bonus("bonus", 145, 207),
            Bonus("bonus", 221, 207),
        ])

        self.register_map("donjon", portals=[
            Portal(from_world='donjon', origin_point='exit_donjon', target_world='bones',
                   teleport_point='spawn_donjon_bones'),
            Portal(from_world='donjon', origin_point='enter_donjon_lab', target_world='labyrinthe',
                   teleport_point='spawn_donjon_lab')
        ], monsters=[
            Monsters("boss", nb_points=9, speed=1, attaque=10),
            Monsters("boss1", nb_points=4, speed=1, attaque=2),
            Monsters("boss2", nb_points=2, speed=2, attaque=2),
            Monsters("boss3", nb_points=4, speed=1, attaque=2),

        ], fire_ball=[
            FireBall("comet", 678, 326),
            FireBall("comet", 678, 389),
            FireBall("comet", 678, 451),
            FireBall("comet", 709, 582),
            FireBall("comet", 709, 647),
            FireBall("comet", 709, 711),

        ], bonus=[
            Bonus("bonus", 608, 176),
            Bonus("bonus", 399, 64),
            Bonus("bonus", 175, 161),
            Bonus("bonus", 81, 80),
            Bonus("bonus", 81, 434),
            Bonus("bonus", 320, 379),
            Bonus("bonus", 575, 339),
            Bonus("bonus", 671, 640),
            Bonus("bonus", 468, 720),
            Bonus("bonus", 254, 638),
            Bonus("bonus", 178, 728),

        ], hearts=[
            Heart("coeur", 160, 113)
        ])

        self.register_map("bones", portals=[
            Portal(from_world='bones', origin_point='exit_bones', target_world='hiver',
                   teleport_point='spawn_hiver'),
            Portal(from_world='bones', origin_point='enter_bones_donjon', target_world='donjon',
                   teleport_point='spawn_bones_donjon')
        ], monsters=[
            Monsters("boss", nb_points=6, speed=2, attaque=2),
            Monsters("boss1", nb_points=4, speed=1, attaque=2),
            Monsters("boss2", nb_points=6, speed=2, attaque=2),
            Monsters("boss3", nb_points=2, speed=1, attaque=2),
            Monsters("boss4", nb_points=4, speed=2, attaque=3),
            Monsters("boss5", nb_points=2, speed=2, attaque=3),
            Monsters("boss6", nb_points=8, speed=3, attaque=2),
            Monsters("boss7", nb_points=2, speed=2, attaque=2),

        ], bonus=[
            Bonus("bonus", 698, 458),
            Bonus("bonus", 474, 718),
            Bonus("bonus", 118, 757),
            Bonus("bonus", 99, 506),
            Bonus("bonus", 322, 571),
            Bonus("bonus", 383, 457),
            Bonus("bonus", 593, 203),
            Bonus("bonus", 380, 377),
            Bonus("bonus", 144, 345),
            Bonus("bonus", 85, 97),
            Bonus("bonus", 380, 68),

        ], fire_ball=[
            FireBall("comet", 756, 341),

        ])

        self.register_map("hiver", portals=[
            Portal(from_world='hiver', origin_point='exit_hiver', target_world='world',
                   teleport_point='enter_hiver_exit'),
            Portal(from_world='hiver', origin_point='enter_hiver_bones', target_world='bones',
                   teleport_point='spawn_hiver_bones'),
            Portal(from_world='hiver', origin_point='enter_hiver_lab2', target_world='labyrinthe2',
                   teleport_point='spawn_hiver_lab2'),
            Portal(from_world='hiver', origin_point='enter_hiver_foret', target_world='foret',
                   teleport_point='spawn_hiver_foret'),
            Portal(from_world='hiver', origin_point='enter_hiver_house4', target_world='house4',
                   teleport_point='spawn_hiver_house4'),
            Portal(from_world='hiver', origin_point='enter_hiver_house5', target_world='house5',
                   teleport_point='spawn_hiver_house5')

        ], monsters=[
            Monsters("boss1", nb_points=5, speed=3, attaque=5),
            Monsters("boss2", nb_points=2, speed=1, attaque=2),
            Monsters("boss3", nb_points=2, speed=2, attaque=5),
            Monsters("boss4", nb_points=6, speed=2, attaque=5),
            Monsters("boss5", nb_points=4, speed=1, attaque=5),
            Monsters("boss6", nb_points=6, speed=2, attaque=5),

        ], bonus=[
            Bonus("bonus", 192, 160),
            Bonus("bonus", 338, 32),
            Bonus("bonus", 639, 208),
            Bonus("bonus", 592, 656),
            Bonus("bonus", 623, 47),
            Bonus("bonus", 224, 608),
        ])

        self.register_map("labyrinthe2", portals=[
            Portal(from_world='labyrinthe2', origin_point='enter_lab2_hiver', target_world='hiver',
                   teleport_point='spawn_lab2_hiver'),
            Portal(from_world='labyrinthe2', origin_point='enter_lab2_hall', target_world='hall',
                   teleport_point='spawn_lab2_hall'),
        ], monsters=[
            Monsters("boss", nb_points=4, speed=1, attaque=5),
            Monsters("boss1", nb_points=6, speed=2, attaque=3),
            Monsters("boss2", nb_points=18, speed=3, attaque=2),
            Monsters("boss3", nb_points=4, speed=2, attaque=5),
            Monsters("boss4", nb_points=2, speed=1, attaque=5),
            Monsters("boss5", nb_points=2, speed=2, attaque=5),
            Monsters("boss6", nb_points=2, speed=2, attaque=5),
            Monsters("boss7", nb_points=4, speed=2, attaque=5),

        ],  bonus=[
            Bonus("bonus", 704, 739),
            Bonus("bonus", 742, 651),
            Bonus("bonus", 752, 398),
            Bonus("bonus", 330, 433),
            Bonus("bonus", 171, 638),
            Bonus("bonus", 153, 403),
            Bonus("bonus", 406, 145),
            Bonus("bonus", 759, 227),
            Bonus("bonus", 163, 127),
            Bonus("bonus", 712, 146),
            Bonus("bonus", 340, 21),

        ], hearts=[
            Heart("coeur", 33, 160)
        ])

        self.register_map("hall", portals=[
            Portal(from_world='hall', origin_point='enter_hall_lab2', target_world='labyrinthe2',
                   teleport_point='spawn_hall_lab2'),
            Portal(from_world='hall', origin_point='enter_hall_foret', target_world='foret',
                   teleport_point='spawn_hall_foret'),

        ], fire_ball=[
            FireBall("comet", 742, 100),
            FireBall("comet", 742, 170),
            FireBall("comet", 742, 230),
            FireBall("comet", 742, 292),
            FireBall("comet", 742, 358),
            FireBall("comet", 742, 422),
            FireBall("comet", 742, 490),
            FireBall("comet", 742, 533),
            FireBall("comet", 742, 598),
        ],  bonus=[
            Bonus("bonus", 158, 188),
            Bonus("bonus", 362, 138),
            Bonus("bonus", 538, 114),
            Bonus("bonus", 587, 272),
            Bonus("bonus", 417, 294),
            Bonus("bonus", 164, 264),
            Bonus("bonus", 190, 385),
            Bonus("bonus", 378, 430),
            Bonus("bonus", 550, 388),

        ])

        self.register_map("foret", portals=[
            Portal(from_world='foret', origin_point='enter_foret_hall', target_world='hall',
                   teleport_point='spawn_foret_hall'),
            Portal(from_world='foret', origin_point='enter_foret_world', target_world='world',
                   teleport_point='spawn_foret_world'),
            Portal(from_world='foret', origin_point='enter_foret_hiver', target_world='hiver',
                   teleport_point='spawn_foret_hiver'),

        ], monsters=[
            Monsters("boss", nb_points=2, speed=1, attaque=5),
            Monsters("boss1", nb_points=4, speed=2, attaque=3),
            Monsters("boss2", nb_points=2, speed=3, attaque=2),
            Monsters("boss3", nb_points=2, speed=2, attaque=5),
            Monsters("boss4", nb_points=2, speed=1, attaque=5),
            Monsters("boss5", nb_points=6, speed=2, attaque=5),
            Monsters("boss6", nb_points=2, speed=2, attaque=5),
            Monsters("boss7", nb_points=2, speed=2, attaque=5),

        ],  bonus=[
            Bonus("bonus", 82, 82),
            Bonus("bonus", 228, 81),
            Bonus("bonus", 116, 310),
            Bonus("bonus", 66, 660),
            Bonus("bonus", 271, 756),
            Bonus("bonus", 439, 355),
            Bonus("bonus", 752, 50),
            Bonus("bonus", 611, 392),
            Bonus("bonus", 595, 657),
        ])

        self.teleport_player('player')
        self.teleport_npcs()
        self.teleport_monsters()
        self.teleport_bonus()
        self.teleport_ball()
        self.teleport_heart()
        self.teleport_big_monster()

    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC:
                dialog_box.execute(sprite.dialog)

    def check_collisions(self):
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        for sprite in self.get_group().sprites():
            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1

            if type(sprite) is Monsters:
                if sprite.feet.colliderect(self.player.rect):
                    self.player.damages(sprite.attaque)
                    self.sound.play('power_down')
                    return self.player.health

            if type(sprite) is not Bonus and type(sprite) is not FireBall and type(sprite) is not Heart and \
                    sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

            if type(sprite) is not Bonus and type(sprite) is not FireBall and type(sprite) is not Heart and \
                    sprite.feet.collidelist(self.get_life()) > -1:
                self.player.up_life()
                self.sound.play('power_up')

            if sprite.feet.collidelist(self.get_poison()) > -1:
                damage = 0.5
                print(damage)
                self.player.damages(damage)
                return self.player.health

            if type(sprite) is Bonus:
                if self.player.rect.colliderect(sprite.rect):
                    sprite.erase()
                    self.player.add_bonus(sprite.value)
                    self.sound.play('bonus')

            if type(sprite) is Heart:
                if self.player.rect.colliderect(sprite.rect):
                    sprite.erase()
                    self.player.add_life()
                    self.sound.play('coeur')

            if type(sprite) is FireBall:
                if self.player.rect.colliderect(sprite.rect):
                    self.player.damages(sprite.value)
                    self.sound.play('power_down')
                    sprite.load_position()
                    return self.player.health

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[], monsters=[], bonus=[],
                     fire_ball=[], hearts=[], big_monster=[]):

        # chager le carte
        tmx_data = pytmx.util_pygame.load_pygame(f'../maps/{name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definition de liste de collisions
        walls = []
        life = []
        poison = []

        for obj in tmx_data.objects:
            if obj.name == 'collision':
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == 'life':
                life.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == 'poison':
                poison.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de claques
        group = pyscroll.PyscrollGroup(map_layer, default_layer=5)
        group.add(self.player)

        # ajout de PNJ
        for npc in npcs:
            group.add(npc)

        # ajout de monstres
        for monster in monsters:
            group.add(monster)

        # ajout des bonus
        for bon in bonus:
            group.add(bon)

        # ajout boule de feu
        for ball in fire_ball:
            group.add(ball)

        # ajout coeur de vie
        for heart in hearts:
            group.add(heart)

        # ajout grands montres
        for monster in big_monster:
            group.add(monster)

        # création d'1 objet map
        self.maps[name] = Map(name, walls, life, poison, group, tmx_data, portals, npcs,
                              monsters, bonus, fire_ball, hearts, big_monster)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def get_life(self):
        return self.get_map().life

    def get_poison(self):
        return self.get_map().poison

    def get_object(self, name):
        return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def teleport_monsters(self):
        for map in self.maps:
            map_data = self.maps[map]
            monsters = map_data.monsters

            for monster in monsters:
                monster.load_points(map_data.tmx_data)
                monster.teleport_spawn()

    def teleport_big_monster(self):
        for map in self.maps:
            map_data = self.maps[map]
            big_monster = map_data.big_monster

            for monster in big_monster:
                monster.load_points(map_data.tmx_data)
                monster.teleport_spawn()

    def teleport_bonus(self):
        for map in self.maps:
            map_data = self.maps[map]
            bonus = map_data.bonus
            for bon in bonus:
                bon.load_position()

    def teleport_ball(self):
        for map in self.maps:
            map_data = self.maps[map]
            fire_ball = map_data.fire_ball

            for ball in fire_ball:
                ball.load_position()

    def teleport_heart(self):
        for map in self.maps:
            map_data = self.maps[map]
            hearts = map_data.hearts

            for heart in hearts:
                heart.load_position()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()

        for npc in self.get_map().npcs:
            npc.move()
        for monster in self.get_map().monsters:
            monster.move()
        for ball in self.get_map().fire_ball:
            ball.move()
        for monster in self.get_map().big_monster:
            monster.move()
