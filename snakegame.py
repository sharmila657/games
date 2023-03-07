'''
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
'''
from random import randrange
import turtle
from turtle import *

from freegames import square, vector


food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)
bgcolor("green")

#score
score=0;
delay=0.1

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score:",align="center",font=("Courier",24,"bold"))


def change(x,y):
    #change snake direction
    aim.x=x
    aim.y=y
    
def inside(head):
    #return True if head inside boundaries
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    #move snake forward one step
    head=snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9,'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('snake:',len(snake))
        food.x=randrange(-15,15)*10
        food.y=randrange(-15,15)*10        

    else:
        snake.pop(0)    

    clear()

    for body in snake:
        square(body.x,body.y,9,'black')

    square(food.x,food.y, 9, 'red')  
    update()
    ontimer(move, 250)

def gameLoop():
    game_over = False
    game_close 





setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10,0),'Right')
onkey(lambda: change(-10,0),'Left')
onkey(lambda: change(0,10),'Up')
onkey(lambda: change(0,-10),'Down')
move()
done()










