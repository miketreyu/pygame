import pygame
import constant

class Character():
    def __init__(self, x, y, animations):
        self.flip = False
        self.animations = animations
        #animated immage shown at the moment
        self.frame_index = 0
        #here we store in miliseconds the actual time that has passed since we began playing
        self.update_time = pygame.time.get_ticks()
        self.image = animations[self.frame_index]
        self.forma =  self.image.get_rect() #pygame.Rect(0, 0, constant.WIDTH_CHARACTER, constant.HEIGHT_CHARACTER)
        self.forma.center = (x, y)

    def movement(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def update(self):
        cooldown_animation = 100
        self.image = self.animations[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animations):
            self.frame_index = 0

    def draw(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(image_flip, self.forma)
        #pygame.draw.rect(interfaz, constant.COLOR_CHARACTER, self.forma, 1)






