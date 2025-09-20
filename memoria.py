"""Memory, puzzle game with emojis instead of numbers.

Cambios:
1. Contar y desplegar el número de taps.
2. Detectar cuando todos los cuadros se han destapado.
3. Centrar el símbolo en el cuadro.
4. Usar emojis en lugar de números para hacerlo más divertido.
"""

from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')

# Lista de 32 emojis distintos, duplicados para hacer pares
tiles = (['🍎','🍌','🍇','🍉','🍒','🍍','🥑','🥕',
          '🥦','🍓','🍑','🍋','🥥','🍊','🍈','🍐',
          '🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼',
          '🐨','🐯','🦁','🐮','🐷','🐸','🐵','🐤'] * 2)

state = {'mark': None}
hide = [True] * 64
taps = 0  # contador de taps


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    spot = index(x, y)
    mark = state['mark']
    taps += 1  # contar taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # centrar en el cuadro de 50x50
        color('black')
        write(tiles[mark], align="center", font=('Arial', 20, 'normal'))

    # Mostrar número de taps
    up()
    goto(-180, 180)
    color('blue')
    write(f'Taps: {taps}', font=('Arial', 15, 'bold'))

    # Detectar si ya ganó
    if all(not h for h in hide):
        up()
        goto(-50, 0)
        color('green')
        write("¡Ganaste! 🎉", font=('Arial', 24, 'bold'))
        update()
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
