import turtle
import Enemigo as e
import time 
import Nave as n
import Bala as b

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Juego de Nave")







nave = n.Nave()
screen.listen()
screen.onkeypress(nave.mover_abajo,"Down")
screen.onkeypress(nave.mover_arriba, "Up")
screen.onkeypress(nave.mover_izquierda, "Left")
screen.onkeypress(nave.mover_derecha, "Right")
screen.onkeypress(nave.disparar, "space")


def crearEnemigo():
    enemigo = e.Enemigo()
    return enemigo


texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,265)
texto.write("Score:0",align="center",font=("Courier",24,"normal"))



endingMessage = turtle.Turtle()
endingMessage.speed(0)
endingMessage.color("white")
endingMessage.penup()
endingMessage.hideturtle()
endingMessage.goto(0,0)



enemigos = []
score = int(0)
game = "start"

while game != "stop":
    if len(enemigos) < 7:
        enemigo = crearEnemigo()
        enemigos.append(enemigo)
    for bala in nave.getscreen().turtles():
        if isinstance(bala, b.Bala):
            bala.mover()

            for enemigo in enemigos:
                if bala.distance(enemigo) < 20:  
                    score+=10
                    texto.clear()
                    texto.write("Score: {}".format(score), align="center",font=("Courier",24,"normal"))
                    enemigos.remove(enemigo) 
                    enemigo.goto(1000,1000)
                    bala.goto(1000,1000)
                    bala.clear()
                    enemigo.clear()

                    break   
    for enemigo in enemigos:
        enemigo.mover()
        if nave.distance(enemigo) < 20:  
            nave.clear()
            time.sleep(2)
            game = "stop"
            endingMessage.write("GAME OVER", align="center" ,font=("Courier",50,"normal"))
            break  

    screen.update()  