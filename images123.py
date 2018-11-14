### animation

import pygame as py
import os
from final_game import man


py.init ()



# player
idle = [py.image.load(os.path.join('player',f'Idle ({i}).png')) for i in range (1,11)]
run_right = [py.image.load(os.path.join('player',f'Run ({i}).png')) for i in range (1,9)]
jump = [py.image.load(os.path.join('player',f'Jump ({i}).png')) for i in range (1,11)]
shoot_idle = [py.image.load(os.path.join('player',f'Shoot ({i}).png')) for i in range (1,5)]
shoot_run = [py.image.load(os.path.join('player',f'RunShoot ({i}).png')) for i in range (1,9)]


# bullets

pows = [py.image.load(os.path.join('player',f'Bullet({i}).png')) for i in range (1,6)]

# fixings

idle = [(py.transform.scale(idle[0],(man.width,man.length))),(py.transform.scale(idle[1],(man.width,man.length))),(py.transform.scale(idle[2],(man.width,man.length))),(py.transform.scale(idle[3],(man.width,man.length))),(py.transform.scale(idle[4],(man.width,man.length))),(py.transform.scale(idle[5],(man.width,man.length))),(py.transform.scale(idle[6],(man.width,man.length))),(py.transform.scale(idle[7],(man.width,man.length))),(py.transform.scale(idle[8],(man.width,man.length))),(py.transform.scale(idle[9],(man.width,man.length)))]
run_right = [(py.transform.scale(run_right[0],(man.width,man.length))),(py.transform.scale(run_right[1],(man.width,man.length))),(py.transform.scale(run_right[2],(man.width,man.length))),(py.transform.scale(run_right[3],(man.width,man.length))),(py.transform.scale(run_right[4],(man.width,man.length))),(py.transform.scale(run_right[5],(man.width,man.length))),(py.transform.scale(run_right[6],(man.width,man.length))),(py.transform.scale(run_right[7],(man.width,man.length)))]
jump = [(py.transform.scale(jump[0],(man.width,man.length))),(py.transform.scale(jump[1],(man.width,man.length))),(py.transform.scale(jump[2],(man.width,man.length))),(py.transform.scale(jump[3],(man.width,man.length))),(py.transform.scale(jump[4],(man.width,man.length))),(py.transform.scale(jump[5],(man.width,man.length))),(py.transform.scale(jump[6],(man.width,man.length))),(py.transform.scale(jump[7],(man.width,man.length))),(py.transform.scale(jump[8],(man.width,man.length))),(py.transform.scale(jump[9],(man.width,man.length)))]
run_left = [(py.transform.flip(run_right[0],True,False)),(py.transform.flip(run_right[1],True,False)),(py.transform.flip(run_right[2],True,False)),(py.transform.flip(run_right[3],True,False)),(py.transform.flip(run_right[4],True,False)),(py.transform.flip(run_right[5],True,False)),(py.transform.flip(run_right[6],True,False)),(py.transform.flip(run_right[7],True,False))]
idle2 = [(py.transform.flip(idle[0],True,False)),(py.transform.flip(idle[1],True,False)),(py.transform.flip(idle[2],True,False)),(py.transform.flip(idle[3],True,False)),(py.transform.flip(idle[4],True,False)),(py.transform.flip(idle[5],True,False)),(py.transform.flip(idle[6],True,False)),(py.transform.flip(idle[7],True,False)),(py.transform.flip(idle[8],True,False)),(py.transform.flip(idle[9],True,False))]
jump2 = [(py.transform.flip(jump[0],True,False)),(py.transform.flip(jump[1],True,False)),(py.transform.flip(jump[2],True,False)),(py.transform.flip(jump[3],True,False)),(py.transform.flip(jump[4],True,False)),(py.transform.flip(jump[5],True,False)),(py.transform.flip(jump[6],True,False)),(py.transform.flip(jump[7],True,False)),(py.transform.flip(jump[8],True,False)),(py.transform.flip(jump[9],True,False))]
shoot_idle = [(py.transform.scale(shoot_idle[0],(man.width,man.length))),(py.transform.scale(shoot_idle[1],(man.width,man.length))),(py.transform.scale(shoot_idle[2],(man.width,man.length))),(py.transform.scale(shoot_idle[3],(man.width,man.length)))]
shoot_idle2 = [(py.transform.flip(shoot_idle[0],True,False)),(py.transform.flip(shoot_idle[1],True,False)),(py.transform.flip(shoot_idle[2],True,False)),(py.transform.flip(shoot_idle[3],True,False))]
shoot_run = [(py.transform.scale(shoot_run[0],(man.width,man.length))),(py.transform.scale(shoot_run[1],(man.width,man.length))),(py.transform.scale(shoot_run[2],(man.width,man.length))),(py.transform.scale(shoot_run[3],(man.width,man.length))),(py.transform.scale(shoot_run[4],(man.width,man.length))),(py.transform.scale(shoot_run[5],(man.width,man.length))),(py.transform.scale(shoot_run[6],(man.width,man.length))),(py.transform.scale(shoot_run[7],(man.width,man.length)))]
shoot_run2 = [(py.transform.flip(shoot_run[0],True,False)),(py.transform.flip(shoot_run[1],True,False)),(py.transform.flip(shoot_run[2],True,False)),(py.transform.flip(shoot_run[3],True,False)),(py.transform.flip(shoot_run[4],True,False)),(py.transform.flip(shoot_run[5],True,False)),(py.transform.flip(shoot_run[6],True,False)),(py.transform.flip(shoot_run[7],True,False))]
pows = [(py.transform.scale(pows[0],(50,50))),(py.transform.scale(pows[1],(50,50))),(py.transform.scale(pows[2],(50,50))),(py.transform.scale(pows[3],(50,50))),(py.transform.scale(pows[4],(50,50)))]
pows2 = [(py.transform.flip(pows[0],True,False)),(py.transform.flip(pows[1],True,False)),(py.transform.flip(pows[2],True,False)),(py.transform.flip(pows[3],True,False)),(py.transform.flip(pows[4],True,False))]

