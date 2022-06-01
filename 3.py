from ast import Lambda
import numpy as np
import matplotlib.pyplot as plt
import math

def Bisec(fun, x_a, x_b, eps=None, steps=100):    
    for n in range(steps + 1):
        xr=(x_a+x_b)/2
        if(xr!=0):
            ea=abs((x_b-x_a)/(x_b+x_a))
        if (ea<eps):
            return xr
        if f(xr) == 0:
            return xr
        
        test=f(x_a)*f(xr)
        if test < 0:
            x_b = xr
        elif test>0 :
            x_a = xr
        else:
            ea=0
        
    return xr

def falsaPosicion(funcion, x_a, x_b,error_r=0.001, iteraciones=100):
    # Se inicializan las variables 
    solucion= None
    contador = 0
    error_calculado = 101
    while contador <= iteraciones and error_calculado>error_r:
        contador+=1
        solucion = x_b-((funcion(x_b)*(x_b - x_a))/(funcion(x_b) - funcion(x_a)))
        error_calculado = abs((solucion - x_a)/solucion)*100
        #Se redefine el nuevo intervalo con los signos 
        if funcion(x_a) * funcion(solucion)>=0: 
            x_a = solucion
        else: 
            x_b = solucion 
            
    print('la solucion aproximada es: {:.3f}'.format(solucion))
    print('encontrada en: {:.0f}'.format(contador) + ' iteraciones')
    print('con un error de:{:.3f}'.format(error_calculado) + '%' )

def Graficar_funcion(fx,inicio, parada,semilla=1000):
    xi=np.linspace(inicio,parada,semilla)
    fi=fx(xi)
    plt.plot(xi,fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.title('Grafica de Funcion')
    plt.legend()
    plt.show()


print("la ecuacion cuadratica tiene esta forma : ")
print("f(x) = ax^5 + bx^4 + cx^3 + dx^2 + ex + f")
a = 0.7
b = -8
c = 44
d = -90
e = 82 
f_ = -25
print("________________________________")
print(f"teniendo una forma de :  {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f_} \n\n")

f = lambda x: (a*x**5)+(b*x**4)+(c*x**3)+(d*x**2)+(e*x)+f_
Graficar_funcion(f,-30,30)
print("________________________________")
print(" -  por metodo de biseccion :")
x=Bisec(f,0.5,1,0.1)
# print(f" - para en la iteracion : {n}")
print(f" - x : {x}")

print("________________________________")
print(" - por metodo de la falsa posicion : ")
falsaPosicion(f,0.5,1,0.02)