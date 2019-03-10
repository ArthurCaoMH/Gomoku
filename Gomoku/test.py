#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
import numpy
background_image = 'qipan.png'
white_image = 'white.png'
black_image = 'black.png'

def WhoWin(x,y,darray):
    num1,num2,num3,num4 = 0,0,0,0
    #判断上下左右左上右上左下右下8个方向
    i = x-1
    while(i>=0):
        if darray[i][y] == 1:
            num1+=1
            i -= 1
        else:
            break
    i = x+1
    while i<19:
        if darray[i][y] == 1:
            num1+=1
            i += 1
        else:
            break
    j =y-1
    while (j >= 0):
        if darray[x][j] == 1:
            num2 += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < 19:
        if darray[x][j] == 1:
            num2 += 1
            j += 1
        else:
            break

    i,j = x-1,y-1
    while(i>=0 and j>=0):
        if darray[i][j] == 1:
            num3 += 1
            i -= 1
            j -= 1
        else :
            break
    i, j = x + 1, y + 1
    while (i < 19 and j < 19):
        if darray[i][j] == 1:
            num3 += 1
            i += 1
            j += 1
        else:
            break

    i, j = x + 1, y - 1
    while (i >= 0 and j >= 0):
        if darray[i][j] == 1:
            num4 += 1
            i += 1
            j -= 1
        else:
            break
    i, j = x - 1, y + 1
    while (i < 19 and j < 19):
        if darray[i][j] == 1:
            num4 += 1
            i -= 1
            j += 1
        else:
            break

#五子胜
    if num1>=4 or num2>=4 or num3 >= 4 or num4 >= 4:
        return True
    else:
        return False

#初始化
pygame.init()
#屏幕、背景图、白黑子转换
screen = pygame.display.set_mode((584, 584), RESIZABLE, 32)
background = pygame.image.load(background_image).convert()
white = pygame.image.load(white_image).convert_alpha()
black = pygame.image.load(black_image).convert_alpha()
#标题画图字体
screen.blit(background, (0,0))
font = pygame.font.SysFont("arial", 40);
pygame.display.set_caption('五子棋')

#zeros()返回19行19列的数组
white_luodian = numpy.zeros((19,19))
black_luodian = numpy.zeros((19,19))

#设置棋盘的所有点的坐标
qipan_list = [(30+i*29-12,30+j*29-12) for i in range(19) for j in range(19)]
#默认黑子先手,转换下棋
transW_B = True
#游戏主循环
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 30 <= x <= 554 and 30 <= y <= 554 and ((x - 30) % 29 <= 12 or (x - 30) % 29 >= 17) and (
                        (y - 30) % 29 <= 12 or (y - 30) % 29 >= 17):
                #四舍五入
                m = int(round((x-30)/29))
                n = int(round((y-30)/29))
                #结果分析
                if transW_B:
                    transW_B = not transW_B
                    screen.blit(black, qipan_list[19*m+n])
                    black_luodian[n][m] = 1
                    if WhoWin(n,m,black_luodian):
                        screen.blit(font.render('Black chess player wins!', True, (0, 0, 0),(0,229,238)), (120, 280))

                else:
                    transW_B = not transW_B
                    screen.blit(white, qipan_list[19 * m + n])
                    white_luodian[n][m] = 1
                    if WhoWin(n,m,white_luodian):
                        screen.blit(font.render('White chess player wins!', True, (255, 255, 255),(0,229,238)), (120, 280))

                qipan_list[19*m+n] = ''

    pygame.display.update()
