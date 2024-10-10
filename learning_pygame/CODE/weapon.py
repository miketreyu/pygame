import pygame
import constant
import math
from bullet import Bullet

class Weapon:
    def __init__(self, image, bullet_image):
        self.bullet_image = bullet_image
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.forma = self.image.get_rect()

    def update(self, character):
        bullet = None
        self.forma.center = character.forma.center
        if character.flip == False:
            self.forma.x = self.forma.x + character.forma.width/3.5
            self.rotate_weapon(False)
        if character.flip == True:
            self.forma.x = self.forma.x - character.forma.width / 3.5
            self.rotate_weapon(True)

        #move the gun with the mouse
        mouse_pos = pygame.mouse.get_pos()
        distance_x = mouse_pos[0] - self.forma.centerx
        distance_y = -(mouse_pos[1] - self.forma.centery)
        self.angle = math.degrees(math.atan2(distance_y, distance_x))

        #notice mouse clicking
        if pygame.mouse.get_pressed()[0]:
            bullet = Bullet(self.bullet_image, self.forma.centerx, self.forma.centery, self.angle)
        return bullet

        #self.forma.y = self.forma.y + 5

    def rotate_weapon(self, rotate):
        if rotate == True:
            image_flip = pygame.transform.flip(self.original_image, True, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)

        else:
            image_flip = pygame.transform.flip(self.original_image, False, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)

    def draw(self, interfaz):
        interfaz.blit(self.image, self.forma)
        # pygame.draw.rect(interfaz, constant.COLOR_GUN, self.forma, 1)
'''
    def rotate_weapon(self, rotate):
        if rotate == True:
            image_flip = pygame.transform.flip(self.original_image, True, False)

        else:
            image_flip = pygame.transform.flip(self.original_image, False, False)
'''

'''
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate()
'''