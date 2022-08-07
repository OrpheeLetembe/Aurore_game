import pygame

from src.player import Entity


class Monsters(Entity):

    def __init__(self, name, nb_points, speed, attaque):
        super().__init__(name, 0, 0)
        self.name = name
        self.attaque = attaque
        self.nb_points = nb_points
        self.points = []
        self.speed = speed
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


class BigMonster(Entity):
    def __init__(self, name, nb_points, speed, attaque):
        super().__init__(name, 0, 0)
        self.name = name
        self.attaque = attaque
        self.nb_points = nb_points
        self.points = []
        self.speed = speed
        self.current_point = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(100),
            'right': self.get_images(200),
            'up': self.get_images(300),
        }

    def get_images(self, y):
        images = []

        for i in range(0, 3):
            x = i * 100
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        image = pygame.Surface([100, 70])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 100, 70))
        return image

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
