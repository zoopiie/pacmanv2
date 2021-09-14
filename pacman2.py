from tkinter import *
from threading import Timer
import keyboard
from random import *
from time import sleep
import copy

levelthree = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
              [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

leveltwo = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

levelone = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

leveltest = [[0 for i in range(25)] for j in range(15)]

width = 0
height = 0
point = 0
level = 1
cellsize = 50
x, y = 0, 0
matrix = 0
check = 0
timeghost = 1
refreshtime = 0.001
changepac = 0.03
multiplicator = 1
life = 3
x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0
y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
ghostbreak = 0
mvtcount = 0
invicible = 0
cheatingvar = 0
anticheatvar = 0
varpac = 0.04
aux1 = 0
cir = 10
playermode = 0
xadv = 0
yadv = 0
ghostwait = 0.08

def ghost1(xx1, yy1, dir, ghostchar):
    global matrix, timeghost, x1, y1, ghostbreak, y, x, life, mvtcount
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    up = [xx1, yy1 - 1]
    down = [xx1, yy1 + 1]
    left = [xx1 - 1, yy1]
    right = [xx1 + 1, yy1]
    if invicible == 0:
        if y == yy1 and x == xx1:
            x = 0
            y = 0
            can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                 fill='black')
            life = life - 1
            countlife.config(text=life)
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
            if life == 0:
                victoryevent.config(text='defeat !!!!')

    aux = 0
    while aux == 0:
        randir = randint(0, 4)
        if randir == 1 and dir != 'down' and yy1 > 0:
            if matrix[up[1]][up[0]] != 1:
                can.create_rectangle(xx1 * cellsize, yy1 * cellsize, (xx1 + 1) * cellsize,
                                     (yy1 + 1) * cellsize, fill='black')
                if matrix[yy1][xx1] == 2:
                    create_circle((xx1 * cellsize + cellsize / 2), (yy1 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx1 * cellsize + cellsize / 2, (yy1 - 1) * cellsize + cellsize / 2, image=ghostchar)
                y1 = y1 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost1, args=(x1, y1, 'up', ghostchar)).start()
        if randir == 2 and dir != 'up' and yy1 < len(matrix)-1:
            if matrix[down[1]][down[0]] != 1:
                can.create_rectangle(xx1 * cellsize, yy1 * cellsize, (xx1 + 1) * cellsize,
                                     (yy1 + 1) * cellsize, fill='black')
                if matrix[yy1][xx1] == 2:
                    create_circle((xx1 * cellsize + cellsize / 2), (yy1 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx1 * cellsize + cellsize / 2, (yy1 + 1) * cellsize + cellsize / 2, image=ghostchar)
                y1 = y1 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost1, args=(x1, y1, 'down', ghostchar)).start()
        if randir == 3 and dir != 'left' and xx1 < len(matrix[0])-1:
            if matrix[right[1]][right[0]] != 1:
                can.create_rectangle(xx1 * cellsize, yy1 * cellsize, (xx1 + 1) * cellsize,
                                     (yy1 + 1) * cellsize, fill='black')
                if matrix[yy1][xx1] == 2:
                    create_circle((xx1 * cellsize + cellsize / 2), (yy1 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx1 + 1) * cellsize + cellsize / 2, yy1 * cellsize + cellsize / 2, image=ghostchar)
                x1 = x1 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost1, args=(x1, y1, 'right', ghostchar)).start()
        if randir == 4 and dir != 'right' and xx1 > 0:
            if matrix[left[1]][left[0]] != 1:
                can.create_rectangle(xx1 * cellsize, yy1 * cellsize, (xx1 + 1) * cellsize,
                                     (yy1 + 1) * cellsize, fill='black')
                if matrix[yy1][xx1] == 2:
                    create_circle((xx1 * cellsize + cellsize / 2), (yy1 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx1 - 1) * cellsize + cellsize / 2, yy1 * cellsize + cellsize / 2, image=ghostchar)
                x1 = x1 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost1, args=(x1, y1, 'left', ghostchar)).start()


def ghost2(xx2, yy2, dir, ghostchar):
    global matrix, timeghost, x2, y2, ghostbreak, y, x, life, mvtcount
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    up = [xx2, yy2 - 1]
    down = [xx2, yy2 + 1]
    left = [xx2 - 1, yy2]
    right = [xx2 + 1, yy2]
    if invicible == 0:
        if y == yy2 and x == xx2:
            x = 0
            y = 0
            can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                 fill='black')
            life = life - 1
            countlife.config(text=life)
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
            if life == 0:
                victoryevent.config(text='defeat !!!!')
    aux = 0
    while aux == 0:
        randir = randint(0, 4)
        if randir == 1 and dir != 'down' and yy2 > 0:
            if matrix[up[1]][up[0]] != 1:
                can.create_rectangle(xx2 * cellsize, yy2 * cellsize, (xx2 + 1) * cellsize,
                                     (yy2 + 1) * cellsize, fill='black')
                if matrix[yy2][xx2] == 2:
                    create_circle((xx2 * cellsize + cellsize / 2), (yy2 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx2 * cellsize + cellsize / 2, (yy2 - 1) * cellsize + cellsize / 2, image=ghostchar)
                y2 = y2 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost2, args=(x2, y2, 'up', ghostchar)).start()
        if randir == 2 and dir != 'up' and yy2 < len(matrix)-1:
            if matrix[down[1]][down[0]] != 1:
                can.create_rectangle(xx2 * cellsize, yy2 * cellsize, (xx2 + 1) * cellsize,
                                     (yy2 + 1) * cellsize, fill='black')
                if matrix[yy2][xx2] == 2:
                    create_circle((xx2 * cellsize + cellsize / 2), (yy2 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx2 * cellsize + cellsize / 2, (yy2 + 1) * cellsize + cellsize / 2, image=ghostchar)
                y2 = y2 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost2, args=(x2, y2, 'down', ghostchar)).start()
        if randir == 3 and dir != 'left' and xx2 < len(matrix[0])-1:
            if matrix[right[1]][right[0]] != 1:
                can.create_rectangle(xx2 * cellsize, yy2 * cellsize, (xx2 + 1) * cellsize,
                                     (yy2 + 1) * cellsize, fill='black')
                if matrix[yy2][xx2] == 2:
                    create_circle((xx2 * cellsize + cellsize / 2), (yy2 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx2 + 1) * cellsize + cellsize / 2, yy2 * cellsize + cellsize / 2, image=ghostchar)
                x2 = x2 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost2, args=(x2, y2, 'right', ghostchar)).start()
        if randir == 4 and dir != 'right' and xx2 > 0:
            if matrix[left[1]][left[0]] != 1:
                can.create_rectangle(xx2 * cellsize, yy2 * cellsize, (xx2 + 1) * cellsize,
                                     (yy2 + 1) * cellsize, fill='black')
                if matrix[yy2][xx2] == 2:
                    create_circle((xx2 * cellsize + cellsize / 2), (yy2 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx2 - 1) * cellsize + cellsize / 2, yy2 * cellsize + cellsize / 2, image=ghostchar)
                x2 = x2 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost2, args=(x2, y2, 'left', ghostchar)).start()


def ghost3(xx3, yy3, dir, ghostchar):
    global matrix, timeghost, x3, y3, ghostbreak, y, x, life, mvtcount
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    up = [xx3, yy3 - 1]
    down = [xx3, yy3 + 1]
    left = [xx3 - 1, yy3]
    right = [xx3 + 1, yy3]
    if invicible == 0:
        if y == yy3 and x == xx3:
            x = 0
            y = 0
            can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                 fill='black')
            life = life - 1
            countlife.config(text=life)
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
            if life == 0:
                victoryevent.config(text='defeat !!!!')
    aux = 0
    while aux == 0:
        randir = randint(0, 4)
        if randir == 1 and dir != 'down' and yy3 > 0:
            if matrix[up[1]][up[0]] != 1:
                can.create_rectangle(xx3 * cellsize, yy3 * cellsize, (xx3 + 1) * cellsize,
                                     (yy3 + 1) * cellsize, fill='black')
                if matrix[yy3][xx3] == 2:
                    create_circle((xx3 * cellsize + cellsize / 2), (yy3 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx3 * cellsize + cellsize / 2, (yy3 - 1) * cellsize + cellsize / 2, image=ghostchar)
                y3 = y3 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost3, args=(x3, y3, 'up', ghostchar)).start()
        if randir == 2 and dir != 'up' and yy3 < len(matrix)-1:
            if matrix[down[1]][down[0]] != 1:
                can.create_rectangle(xx3 * cellsize, yy3 * cellsize, (xx3 + 1) * cellsize,
                                     (yy3 + 1) * cellsize, fill='black')
                if matrix[yy3][xx3] == 2:
                    create_circle((xx3 * cellsize + cellsize / 2), (yy3 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx3 * cellsize + cellsize / 2, (yy3 + 1) * cellsize + cellsize / 2, image=ghostchar)
                y3 = y3 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost3, args=(x3, y3, 'down', ghostchar)).start()
        if randir == 3 and dir != 'left' and xx3 < len(matrix[0])-1:
            if matrix[right[1]][right[0]] != 1:
                can.create_rectangle(xx3 * cellsize, yy3 * cellsize, (xx3 + 1) * cellsize,
                                     (yy3 + 1) * cellsize, fill='black')
                if matrix[yy3][xx3] == 2:
                    create_circle((xx3 * cellsize + cellsize / 2), (yy3 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx3 + 1) * cellsize + cellsize / 2, yy3 * cellsize + cellsize / 2, image=ghostchar)
                x3 = x3 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost3, args=(x3, y3, 'right', ghostchar)).start()
        if randir == 4 and dir != 'right' and xx3 > 0:
            if matrix[left[1]][left[0]] != 1:
                can.create_rectangle(xx3 * cellsize, yy3 * cellsize, (xx3 + 1) * cellsize,
                                     (yy3 + 1) * cellsize, fill='black')
                if matrix[yy3][xx3] == 2:
                    create_circle((xx3 * cellsize + cellsize / 2), (yy3 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx3 - 1) * cellsize + cellsize / 2, yy3 * cellsize + cellsize / 2, image=ghostchar)
                x3 = x3 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost3, args=(x3, y3, 'left', ghostchar)).start()


def ghost4(xx4, yy4, dir, ghostchar):
    global matrix, timeghost, x4, y4, ghostbreak, y, x, life, mvtcount
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    up = [xx4, yy4 - 1]
    down = [xx4, yy4 + 1]
    left = [xx4 - 1, yy4]
    right = [xx4 + 1, yy4]
    if invicible == 0:
        if y == yy4 and x == xx4:
            x = 0
            y = 0
            can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                 fill='black')
            life = life - 1
            countlife.config(text=life)
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
            if life == 0:
                victoryevent.config(text='defeat !!!!')
    aux = 0
    while aux == 0:
        randir = randint(0, 4)
        if randir == 1 and dir != 'down' and yy4 > 0:
            if matrix[up[1]][up[0]] != 1:
                can.create_rectangle(xx4 * cellsize, yy4 * cellsize, (xx4 + 1) * cellsize,
                                     (yy4 + 1) * cellsize, fill='black')
                if matrix[yy4][xx4] == 2:
                    create_circle((xx4 * cellsize + cellsize / 2), (yy4 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx4 * cellsize + cellsize / 2, (yy4 - 1) * cellsize + cellsize / 2, image=ghostchar)
                y4 = y4 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost4, args=(x4, y4, 'up', ghostchar)).start()
        if randir == 2 and dir != 'up' and yy4 < len(matrix)-1:
            if matrix[down[1]][down[0]] != 1:
                can.create_rectangle(xx4 * cellsize, yy4 * cellsize, (xx4 + 1) * cellsize,
                                     (yy4 + 1) * cellsize, fill='black')
                if matrix[yy4][xx4] == 2:
                    create_circle((xx4 * cellsize + cellsize / 2), (yy4 * cellsize + cellsize / 2), cir, can)
                can.create_image(xx4 * cellsize + cellsize / 2, (yy4 + 1) * cellsize + cellsize / 2, image=ghostchar)
                y4 = y4 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost4, args=(x4, y4, 'down', ghostchar)).start()
        if randir == 3 and dir != 'left' and xx4 < len(matrix[0])-1:
            if matrix[right[1]][right[0]] != 1:
                can.create_rectangle(xx4 * cellsize, yy4 * cellsize, (xx4 + 1) * cellsize,
                                     (yy4 + 1) * cellsize, fill='black')
                if matrix[yy4][xx4] == 2:
                    create_circle((xx4 * cellsize + cellsize / 2), (yy4 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx4 + 1) * cellsize + cellsize / 2, yy4 * cellsize + cellsize / 2, image=ghostchar)
                x4 = x4 + 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost4, args=(x4, y4, 'right', ghostchar)).start()
        if randir == 4 and dir != 'right' and xx4 > 0:
            if matrix[left[1]][left[0]] != 1:
                can.create_rectangle(xx4 * cellsize, yy4 * cellsize, (xx4 + 1) * cellsize,
                                     (yy4 + 1) * cellsize, fill='black')
                if matrix[yy4][xx4] == 2:
                    create_circle((xx4 * cellsize + cellsize / 2), (yy4 * cellsize + cellsize / 2), cir, can)
                can.create_image((xx4 - 1) * cellsize + cellsize / 2, yy4 * cellsize + cellsize / 2, image=ghostchar)
                x4 = x4 - 1
                aux = 1
                if ghostbreak == 0:
                    Timer(timeghost, ghost4, args=(x4, y4, 'left', ghostchar)).start()


def ghostbreaker():
    global ghostbreak
    ghostbreak = 1 - ghostbreak
    if ghostbreak == 0:
        ghost1(len(matrix[0]) - 1, len(matrix) - 1, '', blinky)
        ghost2(len(matrix[0]) - 1, len(matrix) - 1, '', inky)
        ghost3(len(matrix[0]) - 1, len(matrix) - 1, '', pinky)
        ghost4(len(matrix[0]) - 1, len(matrix) - 1, '', clyde)


def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvasName.create_oval(x0, y0, x1, y1, fill='yellow')


def left():
    global x, y, matrix, check, width, height, point, life, x1, x2, x3, x4, y1, y2, y3, y4, \
        mvtcount, ghostbreak, invicible
    yy = y
    xx = x - 1
    mvtcount += 1
    if playermode == 0:
        if mvtcount == 3:
            ghost1(len(matrix[0]) - 1, len(matrix) - 1, '', blinky)
        if mvtcount == 4:
            ghost2(len(matrix[0]) - 1, len(matrix) - 1, '', inky)
        if mvtcount == 5:
            ghost3(len(matrix[0]) - 1, len(matrix) - 1, '', pinky)
        if mvtcount == 6:
            ghost4(len(matrix[0]) - 1, len(matrix) - 1, '', clyde)
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= y < (len(matrix)) and 0 <= x < (len(matrix[0])):
                x = x - 1
                y = y
                can.create_rectangle((x + 1) * cellsize, y * cellsize, (x + 2) * cellsize,
                                     (y + 1) * cellsize, fill='black')
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmleft)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenleft)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmleft)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenleft)
                sleep(changepac)
                if matrix[y][x] == 2:
                    point += multiplicator
                    point = int(point)
                    countpoint.config(text=point)
                matrix[y][x] = 0
    if invicible == 0:
        if (xx == x1 and yy == y1) or (xx == x2 and yy == y2) or (xx == x3 and yy == y3) or (yy == y4 and xx == x4):
            x = 0
            y = 0
            life = life - 1
            countlife.config(text=life)
            sleep(1)
            can.create_rectangle(xx * cellsize, yy * cellsize, (xx + 1) * cellsize, (yy + 1) * cellsize,
                                 fill='black')
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
    if life == 0:
        ghostbreak = 1
        victoryevent.config(text='defeat !!!!')
        defeatevent()
    if matrix == check:
        victoryevent.config(text="next level")
        ghostbreak = 1
        sleep(4)
        victoryevent.config(text="")
        changelevel()
    if playermode == 1:
        if xadv == x and yadv == y:
            life = life - 1
            x = 0
            y = 0
            countlife.config(text=life)
            if life == 0:
                defeatevent()


def right():
    global x, y, matrix, check, width, height, point, life, x1, x2, x3, x4, y1, y2, y3, y4, \
        mvtcount, ghostbreak, invicible
    yy = y
    xx = x + 1
    mvtcount += 1
    if playermode == 0:
        if mvtcount == 3:
            ghost1(len(matrix[0]) - 1, len(matrix) - 1, '', blinky)
        if mvtcount == 4:
            ghost2(len(matrix[0]) - 1, len(matrix) - 1, '', inky)
        if mvtcount == 5:
            ghost3(len(matrix[0]) - 1, len(matrix) - 1, '', pinky)
        if mvtcount == 6:
            ghost4(len(matrix[0]) - 1, len(matrix) - 1, '', clyde)
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= y < (len(matrix)) and 0 <= x < (len(matrix[0])):
                x = x + 1
                y = y
                can.create_rectangle((x - 1) * cellsize, y * cellsize, x * cellsize,
                                     (y + 1) * cellsize, fill='black')
                can.create_image(x * cellsize + cellsize/2, y * cellsize + cellsize/2, image=pmright)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenright)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmright)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenright)
                sleep(changepac)
                if matrix[y][x] == 2:
                    point += multiplicator
                    point = int(point)
                    countpoint.config(text=point)
                matrix[y][x] = 0
    if invicible == 0:
        if (xx == x1 and yy == y1) or (xx == x2 and yy == y2) or (xx == x3 and yy == y3) or (yy == y4 and xx == x4):
            x = 0
            y = 0
            life = life - 1
            countlife.config(text=life)
            can.create_rectangle(xx * cellsize, yy * cellsize, (xx + 1) * cellsize, (yy + 1) * cellsize,
                                 fill='black')
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
    if life == 0:
        ghostbreak = 1
        victoryevent.config(text='defeat !!!!')
        defeatevent()
    if matrix == check:
        victoryevent.config(text="next level")
        ghostbreak = 1
        sleep(4)
        victoryevent.config(text="")
        changelevel()
    if playermode == 1:
        if xadv == x and yadv == y:
            life = life - 1
            x = 0
            y = 0
            countlife.config(text=life)
            if life == 0:
                defeatevent()


def up():
    global x, y, matrix, check, width, height, point, life, x1, x2, x3, x4, y1, y2, y3, y4, \
        mvtcount, ghostbreak, invicible
    yy = y - 1
    xx = x
    mvtcount += 1
    if playermode == 0:
        if mvtcount == 3:
            ghost1(len(matrix[0]) - 1, len(matrix) - 1, '', blinky)
        if mvtcount == 4:
            ghost2(len(matrix[0]) - 1, len(matrix) - 1, '', inky)
        if mvtcount == 5:
            ghost3(len(matrix[0]) - 1, len(matrix) - 1, '', pinky)
        if mvtcount == 6:
            ghost4(len(matrix[0]) - 1, len(matrix) - 1, '', clyde)
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= y < (len(matrix)) and 0 <= x < (len(matrix[0])):
                x = x
                y = y - 1
                can.create_rectangle(x * cellsize, (y + 1) * cellsize, (x + 1) * cellsize,
                                     (y + 2) * cellsize, fill='black')
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmup)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenup)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmup)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenup)
                sleep(changepac)
                if matrix[y][x] == 2:
                    point += multiplicator
                    point = int(point)
                    countpoint.config(text=point)
                matrix[y][x] = 0
    if invicible == 0:
        if (xx == x1 and yy == y1) or (xx == x2 and yy == y2) or (xx == x3 and yy == y3) or (yy == y4 and xx == x4):
            x = 0
            y = 0
            life = life - 1
            countlife.config(text=life)
            can.create_rectangle(xx * cellsize, yy * cellsize, (xx + 1) * cellsize, (yy + 1) * cellsize,
                                 fill='black')
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
    if life == 0:
        ghostbreak = 1
        victoryevent.config(text='defeat !!!!')
        defeatevent()
    if matrix == check:
        victoryevent.config(text="next level")

        ghostbreak = 1
        sleep(4)
        victoryevent.config(text="")
        changelevel()
    if playermode == 1:
        if xadv == x and yadv == y:
            life = life - 1
            x = 0
            y = 0
            countlife.config(text=life)
            if life == 0:
                defeatevent()


def down():
    global x, y, matrix, check, width, height, point, life, x1, x2, x3, x4, y1, y2, y3, y4, \
        mvtcount, ghostbreak, invicible
    yy = y + 1
    xx = x
    mvtcount += 1
    if playermode == 0:
        if mvtcount == 3:
            ghost1(len(matrix[0]) - 1, len(matrix) - 1, '', blinky)
        if mvtcount == 4:
            ghost2(len(matrix[0]) - 1, len(matrix) - 1, '', inky)
        if mvtcount == 5:
            ghost3(len(matrix[0]) - 1, len(matrix) - 1, '', pinky)
        if mvtcount == 6:
            ghost4(len(matrix[0]) - 1, len(matrix) - 1, '', clyde)
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= y < (len(matrix)) and 0 <= x < (len(matrix[0])):
                x = x
                y = y + 1

                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize,
                                     (y - 1) * cellsize, fill='black')
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmdown)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopendown)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmdown)
                sleep(changepac)
                can.create_rectangle(x * cellsize, y * cellsize, (x + 1) * cellsize, (y + 1) * cellsize,
                                     fill='black')
                sleep(refreshtime)
                can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopendown)
                sleep(changepac)
                if matrix[y][x] == 2:
                    point += multiplicator
                    point = int(point)
                    countpoint.config(text=point)
                matrix[y][x] = 0
    if invicible == 0:
        if (xx == x1 and yy == y1) or (xx == x2 and yy == y2) or (xx == x3 and yy == y3) or (yy == y4 and xx == x4):
            x = 0
            y = 0
            life = life - 1
            countlife.config(text=life)
            can.create_rectangle(xx * cellsize, yy * cellsize, (xx + 1) * cellsize, (yy + 1) * cellsize,
                                 fill='black')
            can.create_image(cellsize / 2, cellsize / 2, image=pmopenright)
    if life == 0:
        ghostbreak = 1
        victoryevent.config(text='defeat !!!!')
        defeatevent()
    if matrix == check:
        victoryevent.config(text="next level")
        ghostbreak = 1
        sleep(4)
        victoryevent.config(text="")
        changelevel()
    if playermode == 1:
        if xadv == x and yadv == y:
            life = life - 1
            x = 0
            y = 0
            countlife.config(text=life)
            if life == 0:
                defeatevent()










def left2():
    global xadv, yadv, matrix, check, width, height, point, life, mvtcount, ghostbreak, invicible, x, y
    yy = yadv
    xx = xadv - 1
    mvtcount += 1
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= yadv < (len(matrix)) and 0 <= xadv < (len(matrix[0])):
                xadv = xadv - 1
                yadv = yadv
                can.create_rectangle((xadv + 1) * cellsize, yadv * cellsize, (xadv + 2) * cellsize,
                                     (yadv + 1) * cellsize, fill='black')
                print(matrix[yadv][xadv + 1], yadv, xadv + 1)
                if matrix[yadv][xadv + 1] == 2:

                    create_circle((xadv + 1) * cellsize + cellsize / 2, yadv * cellsize + cellsize / 2, cir, can)
                can.create_image(xadv * cellsize + cellsize / 2, yadv * cellsize + cellsize / 2, image=ninja)
                sleep(ghostwait)

    if xadv == x and yadv == y:
        life = life - 1
        x = 0
        y = 0
        countlife.config(text=life)
        if life == 0:
            defeatevent()


def right2():
    global xadv, yadv, matrix, check, width, height, point, life, mvtcount, ghostbreak, invicible, x, y
    yy = yadv
    xx = xadv + 1
    mvtcount += 1
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= y < (len(matrix)) and 0 <= xadv < (len(matrix[0])):
                xadv = xadv + 1
                yadv = yadv
                can.create_rectangle((xadv - 1) * cellsize, yadv * cellsize, xadv * cellsize,
                                     (yadv + 1) * cellsize, fill='black')
                print(matrix[yadv][xadv - 1], yadv, xadv - 1)
                if matrix[yadv][xadv - 1] == 2:

                    create_circle((xadv - 1) * cellsize + cellsize / 2, yadv * cellsize + cellsize / 2, cir, can)
                can.create_image(xadv * cellsize + cellsize/2, yadv * cellsize + cellsize/2, image=ninja)
                sleep(ghostwait)

    if xadv == x and yadv == y:
        life = life - 1
        x = 0
        y = 0
        countlife.config(text=life)
        if life == 0:
            defeatevent()


def up2():
    global xadv, yadv, matrix, check, width, height, point, life, mvtcount, ghostbreak, invicible, x, y
    yy = yadv - 1
    xx = xadv
    mvtcount += 1
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= yadv < (len(matrix)) and 0 <= xadv < (len(matrix[0])):
                xadv = xadv
                yadv = yadv - 1
                can.create_rectangle(xadv * cellsize, (yadv + 1) * cellsize, (xadv + 1) * cellsize,
                                     (yadv + 2) * cellsize, fill='black')
                print(matrix[yadv + 1][xadv], yadv + 1, xadv)
                if matrix[yadv + 1][xadv] == 2:

                    create_circle(xadv * cellsize + cellsize / 2, (yadv + 1) * cellsize + cellsize / 2, cir, can)
                can.create_image(xadv * cellsize + cellsize / 2, yadv * cellsize + cellsize / 2, image=ninja)
                sleep(ghostwait)

    if xadv == x and yadv == y:
        life = life - 1
        x = 0
        y = 0
        countlife.config(text=life)
        if life == 0:
            defeatevent()


def down2():
    global xadv, yadv, matrixadv, check, width, height, point, life, mvtcount, ghostbreak, invicible, x, y
    yy = yadv + 1
    xx = xadv
    mvtcount += 1
    if mvtcount >= 150:
        refresh()
        mvtcount = 10
    if 0 <= xx < width and 0 <= yy < height:
        if matrix[yy][xx] == 2 or matrix[yy][xx] == 0:
            if 0 <= yadv < (len(matrix)) and 0 <= xadv < (len(matrix[0])):
                xadv = xadv
                yadv = yadv + 1

                can.create_rectangle(xadv * cellsize, yadv * cellsize, (xadv + 1) * cellsize,
                                     (yadv - 1) * cellsize, fill='black')
                print(matrix[yadv - 1][xadv], yadv - 1, xadv)
                if matrix[yadv - 1][xadv] == 2:

                    create_circle(xadv * cellsize + cellsize / 2, (yadv - 1) * cellsize + cellsize / 2, cir, can)
                can.create_image(xadv * cellsize + cellsize / 2, yadv * cellsize + cellsize / 2, image=ninja)
                sleep(ghostwait)
    if xadv == x and yadv == y:
        life = life - 1
        x = 0
        y = 0
        countlife.config(text=life)
        if life == 0:
            defeatevent()








def init():
    global width, height, matrix, check  # params[{'width'=widht}, ]
    if level == 1:
        width = len(levelone[0])
        height = len(levelone)
        check = copy.deepcopy(levelone)
        print('level one ok')
        matrix = copy.deepcopy(levelone)
    if level == 2:
        width = len(leveltwo[0])
        height = len(leveltwo)
        matrix = copy.deepcopy(leveltwo)
        check = copy.deepcopy(leveltwo)
        print("level two ok")
    if level == 3:
        width = len(levelthree[0])
        height = len(levelthree)
        matrix = copy.deepcopy(levelthree)
        check = copy.deepcopy(levelthree)
        print("level three ok")


def create(matrix1):
    global matrix, check, multiplicator, level, x1, x2, x3, x4, y1, y2, y3, y4, yadv, xadv
    init()
    can.delete("all")
    multiplicator = ((level / 10) + 1) * 10
    matrix = matrix1
    y1, y2, y3, y4 = len(matrix) - 1, len(matrix) - 1, len(matrix) - 1, len(matrix) - 1
    x1, x2, x3, x4 = len(matrix[0]) - 1, len(matrix[0]) - 1, len(matrix[0]) - 1, len(matrix[0]) - 1
    can.config(width=len(matrix1[0])*cellsize, height=len(matrix1)*cellsize)
    for i in range(len(matrix1[0])):
        for j in range(len(matrix1)):
            if matrix[j][i] == 1:
                can.create_rectangle(i * cellsize, j * cellsize, (i+1) * cellsize, (j+1) * cellsize, fill='#002eee')
            if matrix[j][i] == 0:
                can.create_rectangle(i * cellsize, j * cellsize, (i + 1) * cellsize, (j + 1) * cellsize, fill='black')
                create_circle((i*cellsize+cellsize/2), (j*cellsize+cellsize/2), cir, can)
    can.create_image(cellsize/2, cellsize/2, image=pmopenright)
    if playermode == 1:
        can.create_image((len(matrix) - 1) * cellsize + cellsize / 2,(len(matrix[0]) - 1) * cellsize +  cellsize / 2, image=ninja)
        yadv = len(matrix) - 1
        xadv = len(matrix[0]) - 1

    matmodif()
    print(matrix)


def refresh():
    can.delete("all")
    can.create_image(x * cellsize + cellsize / 2, y * cellsize + cellsize / 2, image=pmopenright)
    can.create_image(x1 * cellsize + cellsize / 2, y1 * cellsize + cellsize / 2, image=inky)
    can.create_image(x2 * cellsize + cellsize / 2, y2 * cellsize + cellsize / 2, image=blinky)
    can.create_image(x3 * cellsize + cellsize / 2, y3 * cellsize + cellsize / 2, image=pinky)
    can.create_image(x4 * cellsize + cellsize / 2, y4 * cellsize + cellsize / 2, image=clyde)
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                can.create_rectangle(i * cellsize, j * cellsize, (i+1) * cellsize, (j+1) * cellsize, fill='#002eee')
            if matrix[j][i] == 2:
                can.create_rectangle(i * cellsize, j * cellsize, (i + 1) * cellsize, (j + 1) * cellsize, fill='black')
                create_circle((i*cellsize+cellsize/2), (j*cellsize+cellsize/2), cir, can)
            if matrix[j][i] == 0:
                can.create_rectangle(i * cellsize, j * cellsize, (i + 1) * cellsize, (j + 1) * cellsize, fill='black')


def matmodif():
    global matrix, check
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                matrix[j][i] = 2
    matrix[0][0] = 0


def changelevel():
    global level, x, y, matrix, ghostbreak, mvtcount, timeghost
    mvtcount = 0
    ghostbreak = 0
    level += 1
    x, y = 0, 0
    if anticheatvar == 0:
        if level == 2:
            timeghost = timeghost - 0.1
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(leveltwo)
            create(leveltwo)
        if level == 3:
            timeghost = 0.3
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(levelthree)
            create(levelthree)
        if level > 3:
            if timeghost <= 0.2:
                timeghost = timeghost/2
            else:
                timeghost = timeghost - 0.1
            leveldisplay = "%s%s" % ("level ", level)
            countlevel.config(text=leveldisplay)
            matrix = copy.deepcopy(levelthree)
            create(levelthree)
            if playermode == 1:
                can.delete('all')
                win.destroy()
                root.geometry('0x0')
                rt = Toplevel()
                rt.config(bg='black')

                lab = Label(rt, text="pacman est meilleur que le fantome (en vrai c'est de ma faute !)", fg='#00eeee', bg='black', font=('', 40, 'bold')).pack()
    else:
        defeatevent()


def inviciblemode():
    global invicible, cheatingvar, pmup, pmleft, pmdown, pmright, \
        pmopenup, pmopendown, pmopenleft, pmopenright, anticheatvar
    if playermode == 0:
        invicible = 1 - invicible
        cheatingvar += 1
        if invicible == 1:
            pmopenright = chompright
            pmopendown = chompdown
            pmopenleft = chompleft
            pmopenup = chompup
            pmup = greycircle
            pmdown = greycircle
            pmleft = greycircle
            pmright = greycircle
        anticheatvar = 1
        if invicible == 0:
            pmopenright = pmopenright1
            pmopendown = pmopendown1
            pmopenleft = pmopenleft1
            pmopenup = pmopenup1
            pmup = pmup1
            pmdown = pmdown1
            pmleft = pmleft1
            pmright = pmright1


def tricheplus():
    global anticheatvar

    anticheatvar = 0

def discret():
    global cheatingvar
    cheatingvar = 0


def pointplus():
    global point
    point = point + 1523


def morelive():
    global life, cheatingvar, anticheatvar
    life += 1
    cheatingvar += 1
    countlife.config(text=life)
    anticheatvar = 1


def defeatevent():
    can.delete('all')
    win.destroy()
    root.geometry('0x0')
    can.config(width=0, height=0)
    rt = Toplevel()
    rt.config(bg='black')
    if playermode == 0:
        score = "%s%s" % ("ton score est de : ", point)
        lab = Label(rt, text=score, fg='#00eeee', bg='black', font=('', 40, 'bold')).pack()
        if cheatingvar != 0:
            label = Label(rt, text='je sais que tu as triché....', fg='#00eeee', bg='black', font=('', 20, 'bold')).pack()
    else:
        label3 = Label(rt, text='t\'as fait mourir pacman ....', fg='#00eeee', bg='black', font=('', 40, 'bold')).pack()


def test():
    create(leveltest)

def twoplayermode():
    global playermode
    playermode = 1


def clic(event):
    old_x = event.x
    old_y = event.y

    if old_y < 240:
        print('haut')
        root.geometry("1800x1050")
        create(levelone)
    if 480 > old_y > 240:
        twoplayermode()
        root.geometry("1800x1050")
        create(levelone)
        print('twoplayer')
    if old_y > 480:
        print('bas')
        root.destroy()


root = Tk()
root.title('pacman')
root.config(bg='black')

root.geometry('0x0')

win = Toplevel()
win.config(bg='black')
win.geometry('750x750')
win.bind('<Button-1>', clic)
label = Label(win, text='click here to play', bg='black',
              fg='yellow', font=('impact', 35)).pack(pady=75)
label1 = Label(win, text='click here for two players', bg='black',
              fg='yellow', font=('impact', 35)).pack(pady=110)
label2 = Label(win, text='click here to close', bg='black',
              fg='yellow', font=('impact', 35)).place(x=180, y=550)


ninja = PhotoImage(file='ninja.png')
greycircle = PhotoImage(file='greycircle.png')
chompright = PhotoImage(file='chompdroite.png')
chompleft= PhotoImage(file='chompgauche.png')
chompdown = PhotoImage(file='chompbas.png')
chompup = PhotoImage(file='chomphaut.png')
blinky = PhotoImage(file='blinky2.png')
inky = PhotoImage(file='inky2.png')
pinky = PhotoImage(file='pinky2.png')
clyde = PhotoImage(file='clyde2.png')
pmopenup = PhotoImage(file='pacmanopenhaut.png')
pmopendown = PhotoImage(file='pacmanopenbas.png')
pmopenleft = PhotoImage(file='pacmanopengauche.png')
pmopenright = PhotoImage(file='pacmanopendroite.png')
pmup = PhotoImage(file='pacmanhaut.png')
pmdown = PhotoImage(file='pacmanbas.png')
pmleft = PhotoImage(file='pacmangauche.png')
pmright = PhotoImage(file='pacmandroite.png')
pmopenup1 = PhotoImage(file='pacmanopenhaut.png')
pmopendown1 = PhotoImage(file='pacmanopenbas.png')
pmopenleft1 = PhotoImage(file='pacmanopengauche.png')
pmopenright1 = PhotoImage(file='pacmanopendroite.png')
pmup1 = PhotoImage(file='pacmanhaut.png')
pmdown1 = PhotoImage(file='pacmanbas.png')
pmleft1 = PhotoImage(file='pacmangauche.png')
pmright1 = PhotoImage(file='pacmandroite.png')

leveldisplay = "%s%s" % ("level ", level)

countlevel = Label(root, text=leveldisplay, bg='black', fg='#00eeee', font=30)
countlevel.pack(side=LEFT, anchor=NW)
countpoint = Label(root, text=point, bg='black', fg='#00eeee', font=30)
countpoint.pack(side=TOP, anchor=N)
victoryevent = Label(root, text="", bg='black', fg='#00eeee', font=30)
victoryevent.pack(side=RIGHT, anchor=NW)
countlife = Label(root, text=life, bg='black', fg='#00eeee', font=30)
countlife.pack(side=LEFT, anchor=NW)
can = Canvas(root, width=0, height=0, bg='black')
can.pack(side=LEFT)

keyboard.on_press_key("space", lambda _: changelevel())
keyboard.on_press_key("up", lambda _: up())
keyboard.on_press_key("down", lambda _: down())
keyboard.on_press_key("left", lambda _: left())
keyboard.on_press_key("right", lambda _: right())
keyboard.on_press_key("enter", lambda _: inviciblemode())
keyboard.on_press_key("z", lambda _: up2())
keyboard.on_press_key("q", lambda _: left2())
keyboard.on_press_key("s", lambda _: down2())
keyboard.on_press_key("d", lambda _: right2())
keyboard.on_press_key("0", lambda _: ghostbreaker())
keyboard.on_press_key("tab", lambda _: morelive())
keyboard.on_press_key("r", lambda _: refresh())
keyboard.on_press_key("ctrl", lambda _: defeatevent())
keyboard.on_press_key("F1", lambda _: tricheplus())
keyboard.on_press_key("F3", lambda _: pointplus())
keyboard.on_press_key("F2", lambda _: discret())
keyboard.on_press_key("F12", lambda _: test())


root.mainloop()
