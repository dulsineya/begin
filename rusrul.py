# encoding = utf8

import turtle
import math
import random
import y.helprobot as helprobot


turtle.speed(0)
fhi = ((360) / 7) * math.pi / 180
r = 60

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def colorxy(r, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def baraban(x, y):
    gotoxy(x, y)
    turtle.circle(100)
    gotoxy(x, y + 200)
    colorxy(5,"red")
    gotoxy(x,y)
    for n in range(0, 7):
        Y = 80 + y + r * math.cos(n * fhi)
        X = x + r * math.sin(n * fhi)
        gotoxy(X, Y)
        turtle.circle(25)
    return n % 7


def rotate(x,y, start):
    for n in range(start, random.randrange(7, 40) ):
        Y = 80 + y + r * math.cos(n * fhi)
        X = x + r * math.sin(n * fhi)
        gotoxy(X, Y)
        turtle.circle(25)
        colorxy(25, "black")
        colorxy(25, "white")

    return n % 7


baraban(100,100)
start = 0
ans = " "
while ans != "нет":
    ans = turtle.textinput("русская рулетка", "сыграть? да/нет ")
    if ans == "да":
        start = rotate(100,100,start)
        if  start == 0:
            turtle.penup()
            gotoxy(200, 200)
            turtle.pendown()
            turtle.write("вы проиграли", font=("Arial", 20, "normal"))
            z = random.randrange(0,3)
            if z == 0:
                helprobot.rand_delete("/Applications/test")
                if helprobot.random_delete("/Applications/test"):
                    gotoxy(200, 100)
                    turtle.write("файл удален", font=("Arial", 20, "normal"))
                else:
                    gotoxy(200,100)
                    print("ошибка удаления")
            elif z == 1:
                if helprobot.rand_dupl("/Applications/test"):
                    gotoxy(200, 100)
                    turtle.write("файл продублирован", font=("Arial", 20, "normal"))
                else:
                    gotoxy(200,100)
                    turtle.write("ошибка дублирования", font=("Arial", 20, "normal"))
            elif z == 2:
                gotoxy(200, 100)
                turtle.write("Вам везёт!", font=("Arial", 20, "normal"))







        # fhi = ((360)/7) * math.pi / 180
        # r = 60
        # for n in range(start, random.randrange(7, 40)):
        #     y  = r * math.cos( n * fhi)
        #     x = -r * math.sin( n * fhi)
        #     gotoxy(x,y)
        #     turtle.circle(25)
        #     colorxy(25, "black")
        #     colorxy(25, "white")

        #
        # gotoxy(x,y)
        # colorxy(25, "black")
        # start = n % 7
        # if start  == 0:
        #     turtle.penup()
        #     gotoxy(200,200)
        #     turtle.write("вы проиграли", font=("Arial", 20, "normal"))
        # else:
        #     pass







