import pygame 
import constant
from character import Character
from weapon import Weapon
from bullet import Bullet

pygame.init()

window = pygame.display.set_mode((constant.WIDTH_WINDOW, constant.HEIGHT_WINDOW))

pygame.display.set_caption('My first pygame')

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image

#Import images
#Characters
animations = []
for i in range (7):
    img = pygame.image.load(f'assets//images//characters//player_01//Player_{i}.png') #.convert_alpha(): se usa para que los png se vean mejor
    img = scale_img(img, constant.SCALE_CHARACTER)
    animations.append(img)

#Weapons
gun_img = pygame.image.load(f'assets//images//weapons//gun.png')
gun_img = scale_img(gun_img, constant.SCALE_GUN)

#Bullets
bullet_img = pygame.image.load(f'assets//images//bullets//bullet_01.png')
bullet_img = scale_img(bullet_img, constant.SCALE_BULLET)

'''
player_image = pygame.image.load('assets//images//characters//player_01//Player_0.png')
player_image = scale_img(player_image, constant.SCALE_CHARACTER)
    (pygame.transform.scale(player_image, (player_image.get_width()*constant.SCALE_CHARACTER, player_image.get_height()*constant.SCALE_CHARACTER)))
'''

#create a character class player
player = Character(250, 350, animations)

#create a weapon class weapon
gun = Weapon(gun_img, bullet_img)

#create a group of sprites
bullet_group = pygame.sprite.Group()


'''
width = 800

height = 600
'''

#define players movement variables
move_up = False
move_down = False
move_left = False
move_right = False

#Controll framerate
clock = pygame.time.Clock()

run = True
while run == True:

    #Run at 60fps
    clock.tick(constant.FPS)

    window.fill(constant.COLOR_BACKGROUND)

    #Calculate players movement
    delta_x = 0
    delta_y = 0

    if move_right == True:
        delta_x = constant.SPEED
    if move_left == True:
        delta_x = -constant.SPEED
    if move_up == True:
        delta_y = -constant.SPEED
    if move_down == True:
        delta_y = constant.SPEED
    #Move player
    player.movement(delta_x, delta_y)

    #updates player status
    player.update()
    #updates weapon status
    bullet = gun.update(player)
    if bullet:
        bullet_group.add(bullet)

    print(bullet_group)

    #draws the player
    player.draw(window)
    #draws weapon
    gun.draw(window)
    #draws bullet
    for bullet in bullet_group:
        bullet.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True

        #We release the key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False


    pygame.display.update()


#def main():
#    print('hola')

pygame.quit()

#if __name__ == '__main__':
#    main()
