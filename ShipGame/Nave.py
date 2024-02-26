import turtle
import Bala as b

class Nave(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.goto(0, -250)
        self.setheading(90)  


    def mover_abajo(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

    def mover_izquierda(self):
        x = self.xcor()
        x -= 10
        self.setx(x)
    
    def mover_arriba(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def mover_derecha(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def disparar(self):
        bala = b.Bala()
        bala.setposition(self.xcor(), self.ycor())
        bala.setheading(90)
        bala.showturtle()