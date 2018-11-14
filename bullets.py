### bullets

from images import *

class bulletss (object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 10 * facing
        self.shootcount = 0
        self.length = 50
        self.width = 50
        self.formatsprites ()
        
    def formatsprites (self):
        self.pows_right = [(py.transform.smoothscale(img,(50,50))) for img in pows]
        self.pows_left = [(py.transform.flip(img,True,False)) for img in self.pows_right]

    def draw(self,win):

        if self.shootcount + 1 == 12:
            self.shootcount = 0

        if self.facing == 1:
            screen.blit (self.pows_right[self.shootcount//3],(self.x+25,self.y-25))
            self.shootcount += 1

        elif self.facing == -1:
            screen.blit (self.pows_left[self.shootcount//3],(self.x-75,self.y-25))
            self.shootcount += 1


