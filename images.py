### animation

import pygame as py
import os

py.init ()



# player
idle = [py.image.load(os.path.join('player',f'Idle ({i}).png')) for i in range (1,11)]
run_right = [py.image.load(os.path.join('player',f'Run ({i}).png')) for i in range (1,9)]
jump = [py.image.load(os.path.join('player',f'Jump ({i}).png')) for i in range (1,11)]
shoot_idle = [py.image.load(os.path.join('player',f'Shoot ({i}).png')) for i in range (1,5)]
shoot_run = [py.image.load(os.path.join('player',f'RunShoot ({i}).png')) for i in range (1,9)]


# bullets

pows = [py.image.load(os.path.join('player',f'Bullet({i}).png')) for i in range (1,6)]

