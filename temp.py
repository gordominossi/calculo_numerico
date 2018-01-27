# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import math


#Classe CONSTRUTORDEGRAFICO
class ConstrutorDeGrafico:

    def __init__(self):
        self.f, self.axarr = plt.subplots(2)
            
    def adicionar(self, X, Y, T, m, tracejado):
        n = 2**(5+m)
        self.axarr[0].set_title('Titulo do gráfico 1')
        self.axarr[0].plot(T, X, tracejado, label='Aprox n = ' + str(n))
        self.axarr[1].set_title('Titulo do gráfico 2')
        self.axarr[1].plot(T, Y, tracejado)


    def mostrar(self):
        plt.xlabel('Eixo T')
        plt.ylabel('Eixo X e Y')
        plt.legend()
        plt.show()
#Fim da classe CONSTRUTORDEGRAFICO



#Classe SIMULADOR
class Simulador:
    
    def __init__(self, m):
        self.m = m
        self.X = []
        self.Y = []
        self.T = []
        self.__simular()
        
        
    def __simular(self):
        #Dados iniciais
        t0 = 0
        tf = 5
        h = (tf - t0)/self.__calcularN()
        
        #Condicoes iniciais
        x0 = 0
        y0 = 0
        
        #Lista dos resultados com C.I. adicionada
        self.X.append(x0)
        self.Y.append(y0)
        self.T.append(t0)
        
        #chamando metodo numerico
        self.__metodoDePassoUnicoBidimensional(h)
    
    
    def __metodoDePassoUnicoBidimensional(self, h):
        for k in range(0, self.__calcularN()):
            t_k1 = self.T[k] + h
            x_k1 = self.X[k] + h * self.__fi(self.__eulerExplicito1(self.X[k], self.Y[k], self.T[k]))
            y_k1 = self.Y[k] + h * self.__fi(self.__eulerExplicito2(self.X[k], self.Y[k], self.T[k]))
            self.T.append(t_k1)
            self.X.append(x_k1)
            self.Y.append(y_k1)
            
    def __calcularN(self):
        return 2**(5+self.m)
            
            
    def __fi(self, f):
        return f
        
        
    def __eulerExplicito1(self, x, y, t):
        return y
    
    
    def __eulerExplicito2(self, x, y, t):
        return -5*y + 4*x + math.sin(10*t)
    
#Fim da classe SIMULADOR
        
    
    
def main():

    construtorDeGrafico = ConstrutorDeGrafico()
    
    sim1 = Simulador(1)
    sim2 = Simulador(3)
    sim3 = Simulador(4)
    #sim4 = Simulador(7) 
    
    construtorDeGrafico.adicionar(sim1.X, sim1.Y, sim1.T, sim1.m, '--')
    construtorDeGrafico.adicionar(sim2.X, sim2.Y, sim2.T, sim2.m, '-.')
    construtorDeGrafico.adicionar(sim3.X, sim3.Y, sim3.T, sim3.m, ':')
    #construtorDeGrafico.adicionar(sim4.X, sim4.Y, sim4.T, sim4.m, 'd')

    
    construtorDeGrafico.mostrar()
    
main()