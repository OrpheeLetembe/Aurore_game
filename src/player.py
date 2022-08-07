import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, name, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'../assets/{name}.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.animation_index = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.clock = 0
        self.speed = 2

    def save_location(self):
        self.old_position = self.position.copy()

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey([0, 0, 0])

        self.clock += self.speed * 8

        if self.clock >= 100:
            self.animation_index += 1

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.clock = 0

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_down(self):
        self.position[1] += self.speed
        self.change_animation('down')

    def move_up(self):
        self.position[1] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_images(self, y):

        images = []

        for i in range(0, 3):
            x = i*32
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image


class Player(Entity):

    def __init__(self):
        super().__init__('player', 0, 0)
        self.health = 100
        self.max_health = 100
        self.number_life = 5
        self.score = 0

    def update_health_bar(self, surface):

        # appliquer la barre de vie
        bar_color = (111, 210, 46)
        back_color = (60, 63, 60)

        health = self.get_health()
        max_health = self.get_max_health()

        bar_position = [10, 5, health, 15]
        back_position = [10, 5, max_health, 15]

        pygame.draw.rect(surface, back_color, back_position)
        pygame.draw.rect(surface, bar_color, bar_position)

        # appliquer background nbe de vie et score
        life_back_color = (255, 255, 255)
        life_back_position = [10, 22, 120, 40]
        pygame.draw.rect(surface, life_back_color, life_back_position)

        # appliquer le nombre de vie
        font = pygame.font.Font("../dialogs/dialog_font.ttf", 15)
        life_number = font.render(f"Vie : {self.number_life}", False, (0, 0, 0))
        surface.blit(life_number, (20, 20))

        # appliquer le score
        font = pygame.font.Font("../dialogs/dialog_font.ttf", 15)
        life_number = font.render(f"Score : {self.score}", False, (0, 0, 0))
        surface.blit(life_number, (20, 40))

    def damages(self, amount):
        self.health -= amount

    def lost_life(self):
        self.number_life -= 1

    def up_life(self):
        self.health = self.max_health

    def add_bonus(self, bonus):
        self.score += bonus

    def get_max_health(self):
        # methode pour l'augmentation de l'arriere plan de la barre de vie
        if self.score >= 50:
            return self.max_health + 50
        else:
            return self.max_health

    def get_health(self):
        # methode pour l'augmentation de la barre de vie
        if self.score >= 50:
            return self.health + 50
        else:
            return self.health

    def add_life(self):
        self.number_life += 1


class NPC(Entity):

    def __init__(self, name, nb_points, dialog):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.speed = 1
        self.name = name
        self.current_point = 0

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
            self.change_animation('down')
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
            self.change_animation('up')
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
            self.change_animation('left')
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()
            self.change_animation('right')

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y,
                               point.width, point.height)
            self.points.append(rect)



