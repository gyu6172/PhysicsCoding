from vpython import *

xaxis = arrow(pos=vec(0, 0, 0), axis=vec(
    10, 0, 0), color=color.red, radius=0.2)
yaxis = arrow(pos=vec(0, 0, 0), axis=vec(
    0, 10, 0), color=color.blue, radius=0.2)
zaxis = arrow(pos=vec(0, 0, 0), axis=vec(
    0, 0, 10), color=color.yellow, radius=0.2)


ball = sphere()
