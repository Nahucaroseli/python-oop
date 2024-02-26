
import turtle

class Bala(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.hideturtle()

    def mover(self):
        y = self.ycor()
        y += 30
        self.sety(y)


        if y > 275:
            self.hideturtle()
            self.clear()
