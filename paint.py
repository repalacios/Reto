"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector

def line(start, end):
    """Draw line from start to end."""
    up(); goto(start.x, start.y); down()
    goto(end.x, end.y)

def square(start, end):
    """Draw square from start to end."""
    up(); goto(start.x, start.y); down()
    begin_fill()
    for _ in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

def circle(start, end):
    """Draw circle from start to end."""
    # radio = |end.x - start.x|
    r = abs(end.x - start.x)
    begin_fill()
    # posiciona al borde derecho del centro y traza círculo
    up(); goto(start.x + r, start.y); setheading(90); down()
    circle(r)
    end_fill()

def rectangle(start, end):
    """Draw rectangle from start to end."""
    up(); goto(start.x, start.y); down()
    begin_fill()
    w = end.x - start.x
    h = end.y - start.y
    for _ in range(2):
        forward(w); left(90)
        forward(h); left(90)
    end_fill()

def triangle(start, end):
    """Draw right triangle using start as (x0,y0) and end as (x1,y1)."""
    up(); goto(start.x, start.y); down()
    begin_fill()
    goto(end.x, start.y)   # base
    goto(end.x, end.y)     # altura
    goto(start.x, start.y) # cierra
    end_fill()

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')  # NUEVO color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
