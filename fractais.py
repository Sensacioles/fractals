import turtle
import matplotlib.pyplot as plt
from random import randint
import numpy as np

'''
Referencias:

Curva de Koch: https://github.com/itsliterallymonique/Koch-Fractal-o_O
Samambaia de Barnsley: https://github.com/itsliterallymonique/Barnsley-Fern
Conjunto de Mandelbrot: https://github.com/itsliterallymonique/Mandelbrot-Set
'''
#Curva de Koch
def koch(tar,ordem,tam):
    if ordem == 0:
        tar.forward(tam)
    else:
        for angulo in [60,-120,60,0]:
            koch(tar,ordem-1,tam/3)
            tar.left(angulo)           
def kochplt():
    ordem = 5
    tam = 200
    tar = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width=1000,height=500)
    tar.penup()
    tar.goto(-500, 150)
    tar.speed(100)
    tar.pendown()
    for i in range(0,3):
        koch(tar,ordem,tam)
        tar.left(-120)
    turtle.Screen().exitonclick()
#end

#Samambaia de Barnsley
def barnsley(x,y):
    for i in range(0, 50000):
        z = randint(1, 100) 
        if z == 1: 
            x.append(0) 
            y.append(0.16*(y[i])) 
        if z>= 2 and z<= 86: 
            x.append(0.85*(x[i]) + 0.04*(y[i])) 
            y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 
        if z>= 87 and z<= 93: 
            x.append(0.2*(x[i]) - 0.26*(y[i])) 
            y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
        if z>= 94 and z<= 100: 
            x.append(-0.15*(x[i]) + 0.28*(y[i])) 
            y.append(0.26*(x[i]) + 0.24*(y[i])+0.44)
    plt.scatter(x, y, s = 0.2, c ='#5dbb63') 
    plt.axis("off")
    plt.savefig('barnsley_fern.png', dpi=300, bbox_inches='tight')
    plt.show()
#end

#Conjunto de Mandelbrot
def mandelbrot(c,z):
    itera = 150
    cont = 0
    for a in range(itera):
        if(abs(z)<4):
            z = z**2+c
            cont += 1
    return cont
def mandelbrot_set(x, y):
    m = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0,0)
            cont = mandelbrot(c, z)
            m[i,j] = cont
    return m
def mandelbrotplt(lin,col,x,y,m):
    x = np.linspace(-2, 1, lin)
    y = np.linspace(-1, 1, col)
    m = mandelbrot_set(x, y)
    plt.imshow(m.T, cmap = "magma")
    plt.axis("off")
    plt.savefig('mandelbrot_set.png', dpi=300, bbox_inches='tight')
    plt.show()
#end

#Para executar a Curva de Koch, tire os comentários em bloco
'''
kochplt()
'''
#Para executar a Samambaia de Barnsley, tire os comentários em bloco
'''
x = [0]
y = [0]
barnsley(x,y)
'''
#Para executar o Conjunto de Mandelbrot, tire os comentários em bloco
'''
lin = 1000
col = 1000
x = [0]
y = [0]
mandelbrotplt(lin,col,x,y,mandelbrot_set(x,y))
'''
