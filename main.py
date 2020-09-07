import turtle
import copy
import time

cordenadas = [[210, 165], [210, 145], [210, 125], [210, 105], [210, 85], [210, 65], [210, 45],
              [210, 25], [210, 5], [210, -15], [210, -35], [210, -55], [210, -75], [210, -95],
              [210, -115], [190, -115], [170, -115], [150, -115], [130, -115], [110, -115],
              [90, -115], [70, -115], [50, -115], [30, -115], [10, -115], [-10, -115], [-30, -115],
              [-50, -115], [-70, -115], [-90, -115], [-110, -115], [-130, -115], [-150, -115],
              [-170, -115], [-170, -95], [-170, -75], [-170, -55], [-170, -35], [-170, -15], [-170, 5],
              [-170, 25], [-170, 45], [-170, 65], [-170, 85], [-170, 105], [-170, 125], [-170, 145],
              [-170, 165], [-150, 165], [-150, 165], [-130, 165], [-110, 165], [-90, 165], [-70, 165], [-50, 165],
              [-30, 165], [-10, 165], [10, 165], [30, 165], [50, 165], [70, 165], [90, 165], [110, 165], [130, 165],
              [150, 165], [170, 165], [190, 165], [-130, -95], [-130, -75], [-130, -55], [-130, -35], [-130, -15],
              [-110, -15],
              [-90, -15], [-70, -15], [-50, -15], [-50, -35], [-50, -55], [-50, -75], [-50, -95], [-50, 5], [-50, 25],
              [-50, 45],
              [-30, 45], [-30, -35], [-10, 5], [10, 5], [10, -15], [10, -35], [10, -55], [10, -75], [-10, -75],
              [10, 25], [10, 45], [10, 65], [10, 85], [-10, 85], [-30, 85], [-50, 85], [-70, 85], [-90, 85],
              [-90, 65], [-90, 45], [-90, 25], [-150, 25], [-130, 25], [-130, 45], [-130, 85], [-130, 105], [-130, 125],
              [-110, 125], [-90, 125], [-70, 125], [-30, 105], [-30, 125], [-30, 145], [30, -75], [50, -75], [50, -55],
              [50, -35], [50, -15], [90, -15], [90, -35], [90, -55], [90, -75], [90, -95], [110, -75], [130, -75],
              [150, -75], [170, -75], [170, -55], [170, -35], [170, -15], [170, 5], [130, -35], [130, -15], [130, 5],
              [130, 25], [110, 25], [90, 25], [70, 25], [50, 25], [50, 45], [30, 85], [50, 85], [10, 125], [30, 125],
              [50, 125], [70, 125], [90, 125], [90, 105], [90, 85], [90, 65], [130, 45], [130, 65], [130, 85],
              [150, 85],
              [170, 85], [170, 125], [170, 105], [130, 125], [130, 145], [170, 45], [190, 45]]

# Wn setup
wn = turtle.Screen()
wn.title("pathfinding")
wn.setup(width=450, height=350)

# puntero setup

puntero = turtle.Turtle()
puntero.shape("circle")
puntero.color("red")
puntero.up()
puntero.goto(-150, -95)

# bandera setup

bandera = turtle.Turtle()
bandera.shape("circle")
bandera.color("yellow")
bandera.up()
bandera.goto(-150, 65)

# generacion de muros
for pos in cordenadas:
    bot = turtle.Turtle()
    bot.shape("square")
    bot.color("grey")
    bot.speed(0)
    bot.up()
    bot.goto(pos[0], pos[1])


# Movimiento

def arriba():
    puntero.goto(puntero.xcor(),
                 puntero.ycor() + 20)


def abajo():
    puntero.goto(puntero.xcor(),
                 puntero.ycor() - 20)


def derecha():
    puntero.goto(puntero.xcor() + 20,
                 puntero.ycor())


def izq():
    puntero.goto(puntero.xcor() - 20,
                 puntero.ycor())


def nuevo():
    bot = turtle.Turtle()
    bot.shape("square")
    bot.up()

    bot.goto(puntero.xcor(),
             puntero.ycor())
    cordenadas.append([bot.xcor(), bot.ycor()])


def mostrar():
    print([puntero.xcor(), puntero.ycor()])


# Controladores de bandera

def banderaUp():
    bandera.goto(bandera.xcor(),
                 bandera.ycor() + 20)


def banderaDown():
    bandera.goto(bandera.xcor(),
                 bandera.ycor() - 20)


def banderaRight():
    bandera.goto(bandera.xcor() + 20,
                 bandera.ycor())


def banderaLeft():
    bandera.goto(bandera.xcor() - 20,
                 bandera.ycor())


# Pathfinding

class test(object):

    def __init__(self):
        self.__max = 99
        self.__lista = []

    def setMax(self, value):
        self.__max = value

    def getMax(self):
        return self.__max

    def setLista(self, lista):
        self.__lista = lista

    def getLista(self):
        return self.__lista


obj = test();

recurciones = []
nums = []


def buscarBanderaEn(x, y, lista=[]):
    if [x, y] not in cordenadas and len(lista) < obj.getMax():
        if [x, y] not in recurciones:
            recurciones.append([x, y])
            nums.append(len(lista))
        elif nums[recurciones.index([x, y])] > len(lista):
            nums[recurciones.index([x, y])] = len(lista)
        else:
            return 0
        if x == bandera.xcor() and y == bandera.ycor():
            # print(True, lista)
            if len(lista) < obj.getMax():
                obj.setMax(len(lista))
                obj.setLista(lista)

        else:

            # bot = turtle.Turtle()
            # bot.shape("square")
            # bot.color("pink")
            # bot.up()

            # bot.goto(x, y)

            for e in [["arriba", x, y + 20], ["derecha", x + 20, y], ["abajo", x, y - 20], ["izq", x - 20, y]]:
                a = copy.copy(lista)
                a.append(e[0])
                # print(a, "-----", sep="\n")
                buscarBanderaEn(e[1], e[2], a)


def comenzarABuscar():
    timepo = time.time()
    buscarBanderaEn(puntero.xcor(), puntero.ycor())
    final = time.time() - timepo
    print("El proceso a terminado en : " + str(final))
    print("El numero de pasos es : " + str(obj.getMax()))
    for paso in obj.getLista():
        if paso == "arriba":
            arriba()
        elif paso == "derecha":
            derecha()
        elif paso == "izq":
            izq()
        elif paso == "abajo":
            abajo()
    nums.clear()
    recurciones.clear()
    obj.setMax(99)
    obj.setLista([])


# listenners

# debug
wn.onkey(arriba, "Up")
wn.onkey(abajo, "Down")
wn.onkey(derecha, "Right")
wn.onkey(izq, "Left")
wn.onkey(mostrar, "m")

# Normales
wn.onkey(comenzarABuscar, "space")

wn.onkey(banderaUp, "w")
wn.onkey(banderaDown, "s")
wn.onkey(banderaRight, "d")
wn.onkey(banderaLeft, "a")

wn.listen()

wn.exitonclick()
