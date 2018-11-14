import pygame as py
import os, images123

py.init ()

screen = py.display.set_mode ((800,600))


bg = py.image.load('game-assets-game-background-sidescroller.png')
clock = py.time.Clock ()


class player(object):
    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.vel = 5
        self.right = False
        self.left = False
        self.standing = True
        self.idlecount = 0
        self.runcount = 0
        self.jumping = False
        self.jumpcount = 14
        self.direction = 1
        self.jumpingcount = 0
        self.shooting = False
        self.shootingcount = 0

    def draw (self,screen):
        if self.idlecount + 1 >= 30:
            self.idlecount = 0

        if self.runcount + 1 >= 24:
            self.runcount = 0

        if self.jumpingcount + 1 >= 31:
            self.jumpingcount = 0

        if self.shootingcount + 1 >= 9:
            self.shootingcount = 0
        
        if not (self.jumping):
            if not (self.standing):

                if self.right:
                    screen.blit (run_right[self.runcount//3],(self.x,self.y))
                    self.runcount += 1

                    if self.shooting:
                        screen.blit (shoot_run[self.runcount//3],(self.x,self.y))
                        self.runcount += 1
                        self.shooting = False
                        
                elif self.left:
                    screen.blit (run_left[self.runcount//3],(self.x,self.y))
                    self.runcount += 1

                    if self.shooting:
                        screen.blit (shoot_run2[self.runcount//3],(self.x,self.y))
                        self.runcount += 1
                        self.shooting = False
        
            else:
                if self.shooting:
                    if self.direction == 1:
                        screen.blit (shoot_idle[self.shootingcount//2],(self.x,self.y))
                        self.shootingcount += 1
                        
                    elif self.direction == -1:
                        screen.blit (shoot_idle2[self.shootingcount//2],(self.x,self.y))
                        self.shootingcount += 1
                        
                elif self.direction == 1:
                    screen.blit (idle[self.idlecount//3],(self.x,self.y))
                    self.idlecount += 1
                    
                elif self.direction == -1:
                    screen.blit (idle2[self.idlecount//3],(self.x,self.y))
                    self.idlecount += 1

        else:
            if self.direction == 1:
                screen.blit (jump[self.jumpingcount//3],(self.x,self.y))
                self.jumpingcount += 1
                self.runcount = 0

            elif self.direction == -1:
                screen.blit (jump2[self.jumpingcount//3],(self.x,self.y))
                self.jumpingcount += 1
                self.runcount = 0


                                   
class bulletss (object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 10 * facing
        self.shootcount = 0
        self.length = 50
        self.width = 50

    def draw(self,win):

        if self.shootcount + 1 == 12:
            self.shootcount = 0

        if self.facing == 1:
            screen.blit (pows[self.shootcount//3],(self.x+25,self.y-25))
            self.shootcount += 1

        elif self.facing == -1:
            screen.blit (pows2[self.shootcount//3],(self.x-75,self.y-25))
            self.shootcount += 1


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
