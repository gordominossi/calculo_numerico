# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

def gerarGrafico(x, y):
    plt.plot(x,y,label='Primeira linha')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Titulo do gráfico')
    plt.legend()
    plt.show()


def eulerExplicito(x, y, delta_t):
    
    #y_k1 = y_k + delta_t * f(x_k, y_k)
    for k in range(0, n):
        y_k1 = y[k] + delta_t * modelo(x[k], y[k])
        t_k1 = x[k] + delta_t
        x.append(t_k1)
        y.append(y_k1)        
        

def modelo(x_k, y_k):
    return y_k


def main():
    
    #Dados iniciais
    t0 = 0
    tf = 10
    n = 32
    y0 = 1
    delta_t = (tf - t0)/n
    
    #Lista dos resultados com C.I. adicionada
    x = [t0]
    y = [y0]
    
    #metodo numerico
    eulerExplicito(x, y, delta_t)
    
    #saida
    gerarGrafico(x, y)
    
main()