# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt



#Classe CONSTRUTORDEGRAFICO
class ConstrutorDeGrafico:

    def adicionar(self, X, Y, T, n, tracejado):
        plt.plot(T, X, tracejado, label='Aprox n = ' + str(n))
        plt.plot(T, Y, tracejado)


    def mostrar(self):
        plt.xlabel('Eixo T')
        plt.ylabel('Eixo X e Y')
        plt.title('Titulo do gráfico')
        plt.legend()
        plt.show()
#Fim da classe CONSTRUTORDEGRAFICO



#Classe SIMULADOR
class Simulador:
    
    def __init__(self, n):
        self.n = n
        self.X = []
        self.Y = []
        self.T = []
        self.__simular()
        
        
    def __simular(self):
        #Dados iniciais
        t0 = 0
        tf = 40
        h = (tf - t0)/self.n
        
        #Condicoes iniciais
        x0 = 1
        y0 = 0.5
        
        #Lista dos resultados com C.I. adicionada
        self.X.append(x0)
        self.Y.append(y0)
        self.T.append(t0)
        
        #chamando metodo numerico
        self.__metodoDePassoUnicoBidimensional(h)
    
    
    def __metodoDePassoUnicoBidimensional(self, h):
        for k in range(0, self.n):
            t_k1 = self.T[k] + h
            x_k1 = self.X[k] + h * self.__eulerExplicito1(self.X[k], self.Y[k])
            y_k1 = self.Y[k] + h * self.__eulerExplicito2(self.X[k], self.Y[k])
            self.T.append(t_k1)
            self.X.append(x_k1)
            self.Y.append(y_k1)
            
            
    def __eulerExplicito1(self, x, y):
        return (x * 1.0 - (x * y * 0.5) )
    
    
    def __eulerExplicito2(self, x, y):
        return (y * (-0.75) + (y * x * 0.5) )
    
#Fim da classe SIMULADOR
        
    
    
def main():

    construtorDeGrafico = ConstrutorDeGrafico()
    
    sim1 = Simulador(1024)
    sim2 = Simulador(512)
    sim2 = Simulador(256) 
    
    construtorDeGrafico.adicionar(sim1.X, sim1.Y, sim1.T, sim1.n, ':')
    construtorDeGrafico.adicionar(sim2.X, sim2.Y, sim2.T, sim2.n, '-.')
    construtorDeGrafico.adicionar(sim2.X, sim2.Y, sim2.T, sim2.n, '--')
    
    construtorDeGrafico.mostrar()
    
main()
