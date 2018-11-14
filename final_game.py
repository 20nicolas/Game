import pygame as py
import os
from players import *
from bullets import *

py.init ()

screen = py.display.set_mode ((800,600))


bg = py.image.load(os.path.join('backgrounds','game-assets-game-background-sidescroller.png'))
clock = py.time.Clock ()


#class enemies (object):
        
      
def drawGameScreen ():
    screen.blit(bg,(0,0))
    man.draw (screen)
    for bullet in bullets:
        bullet.draw (screen)    

    py.display.update ()

##main loop

man = player (100,430,100,100)
game = True
bullets = []
shootloop = 0

         
while game:
    clock.tick (30)

    if shootloop > 0:
        shootloop += 1

    if shootloop > 5:
        shootloop = 0
     
    for event in py.event.get():
        if event == py.QUIT:
            game = False

    keys = py.key.get_pressed ()

    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel

        else:
            bullets.remove (bullet)

    

        
    if keys[py.K_RIGHT] and man.x <= 700:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
        man.idlecount = 0
        man.direction = 1

    elif keys[py.K_LEFT] and man.x >= 0:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.standing = False
        man.idlecount = 0
        man.direction = -1
        
    else:
        man.standing = True
        man.shooting = False

    if keys [py.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1

        elif man.right:
            facing = 1

        if len(bullets) < 5:
            man.standing = True
            man.shooting = True
            bullets.append(bulletss(round(man.x + man.length//2), round(man.y + man.length//2), facing))

        shootloop = 1

    if not(man.jumping):
        if keys[py.K_UP]:
            man.jumping = True
            man.right = False
            man.left = False
            man.standing = False
            man.walkcount = 0
    else:
        if man.jumpcount >= -14:
            neg = 1
            if man.jumpcount < 0:
                neg = -1
            man.y -= (man.jumpcount ** 2) * 0.15 * neg
            man.jumpcount -= 1
        else:
            man.jumping = False
            man.jumpcount = 14    

    drawGameScreen ()
