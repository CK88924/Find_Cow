# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:40:57 2022

@author: kevin
"""
import pygame as pg
import random as rand
import numpy as np
import math
import sys

def Get_Target(width,height):
    Size =[]
    for x in range(0,(width + 1)):
        for y in range(0,(height + 1)):
            Size.append([x,y])
        target = rand.choice(Size)
    print(target)
    return target

def Distance(pos1,pos2):
        p1 = np.array(pos1)
        p2 = np.array(pos2)
        p3 = p2-p1
        p4 = math.hypot(p3[0],p3[1])
        print(int(p4))
        return int (p4)

def Game():
    run = True
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load('cowsound.mp3')
    width, height = 640, 480
    target = Get_Target(width, height)
    Get_Target(width, height)                      
    screen = pg.display.set_mode((width, height)) 
    pg.display.set_caption("Find cow!!")
  
           

    #建立畫布bg
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,255))           #白色
    #顯示
    screen.blit(bg, (0,0))
    pg.display.update()
    
    while run == True:
        # get():获取事件的返回值
        for event in pg.event.get():
            # 判断事件是否是退出事件，是则退出
            if event.type == pg.QUIT:
                # 先退出pygame窗口，再退出程序
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEMOTION:
                print(event.pos)
                dis = Distance(event.pos, target)
                if dis == 0:
                    print("find it!!")
                    run = False
                elif dis >= 1 and dis <= 199:
                    pg.mixer.music.set_volume(1.0)
                    pg.mixer.music.play()
                elif dis >= 200 and dis <= 299:
                    pg.mixer.music.set_volume(0.9)
                    pg.mixer.music.play()
                    
                elif dis >= 300 and dis <= 399:
                    pg.mixer.music.set_volume(0.8)
                    pg.mixer.music.play()
                    
                elif dis >= 400 and dis <= 499:
                    pg.mixer.music.set_volume(0.7)
                    pg.mixer.music.play()
                    
                elif dis >= 500 and dis <= 599:
                    pg.mixer.music.set_volume(0.6)
                    pg.mixer.music.play()
                    
                elif dis >= 600 and dis <= 699:
                    pg.mixer.music.set_volume(0.5)
                    pg.mixer.music.play()
                    
                elif dis >= 700 and dis <= 799:
                    pg.mixer.music.set_volume(0.4)
                    pg.mixer.music.play()
                   
                elif dis >= 800 and dis <= 899:
                    pg.mixer.music.set_volume(0.3)
                    pg.mixer.music.play()
                    
                elif dis >= 900 and dis <= 999:
                    pg.mixer.music.set_volume(0.2)
                    pg.mixer.music.play()
                   
                else:
                    pg.mixer.music.set_volume(0.1)
                    pg.mixer.music.play()
                    
                pg.display.update()
    pg.quit()
    sys.exit()

if __name__ == '__main__':
   Game()