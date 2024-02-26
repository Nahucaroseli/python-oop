import turtle
import random

class Enemigo(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("triangle")
        self.penup()
        self.speed(3)
        number = random.randint(-270,270)
        self.setheading(270)
        self.goto(number,250)
        
    def mover(self):
        y = self.ycor()
        y -= 8
        self.sety(y)
        
        if(y < -275):
            self.hideturtle()
            self.clear()
        