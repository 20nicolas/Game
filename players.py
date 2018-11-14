### player

from images import *

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
        self.formatsprites ()

    def formatsprites (self):
        self.idle_right = [(py.transform.smoothscale(img,(self.width,self.length))) for img in idle]
        self.idle_left = [(py.transform.flip(img,True,False)) for img in self.idle_right]

        self.run_right = [(py.transform.smoothscale(img,(self.width,self.length))) for img in run_right]
        self.run_left = [(py.transform.flip(img,True,False)) for img in self.run_right]

        self.jump_right = [(py.transform.smoothscale(img,(self.width,self.length))) for img in jump]
        self.jump_left = [(py.transform.flip(img,True,False)) for img in self.jump_right]

        self.shoot_idle_right = [(py.transform.smoothscale(img,(self.width,self.length))) for img in shoot_idle]
        self.shoot_idle_left = [(py.transform.flip(img,True,False)) for img in self.shoot_idle_right]

        self.shoot_run_right = [(py.transform.smoothscale(img,(self.width,self.length))) for img in shoot_run]
        self.shoot_run_left = [(py.transform.flip(img,True,False)) for img in self.shoot_run_right]

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
                    screen.blit (self.run_right[self.runcount//3],(self.x,self.y))
                    self.runcount += 1

                    if self.shooting:
                        screen.blit (self.shoot_run_right[self.runcount//3],(self.x,self.y))
                        self.runcount += 1
                        self.shooting = False
                        
                elif self.left:
                    screen.blit (self.run_left[self.runcount//3],(self.x,self.y))
                    self.runcount += 1

                    if self.shooting:
                        screen.blit (self.shoot_run_left[self.runcount//3],(self.x,self.y))
                        self.runcount += 1
                        self.shooting = False
        
            else:
                if self.shooting:
                    if self.direction == 1:
                        screen.blit (self.shoot_idle_right[self.shootingcount//2],(self.x,self.y))
                        self.shootingcount += 1
                        
                    elif self.direction == -1:
                        screen.blit (self.shoot_idle_left[self.shootingcount//2],(self.x,self.y))
                        self.shootingcount += 1
                        
                elif self.direction == 1:
                    screen.blit (self.idle_right[self.idlecount//3],(self.x,self.y))
                    self.idlecount += 1
                    
                elif self.direction == -1:
                    screen.blit (self.idle_left[self.idlecount//3],(self.x,self.y))
                    self.idlecount += 1

        else:
            if self.direction == 1:
                screen.blit (self.jump_right[self.jumpingcount//3],(self.x,self.y))
                self.jumpingcount += 1
                self.runcount = 0

            elif self.direction == -1:
                screen.blit (self.jump_left[self.jumpingcount//3],(self.x,self.y))
                self.jumpingcount += 1
                self.runcount = 0
                                   
