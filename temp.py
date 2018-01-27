# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math


#Classe CONSTRUTORDEGRAFICO
class ConstrutorDeGrafico:

    def __init__(self):
        self.fig = plt.figure()
        self.gs = gridspec.GridSpec(2, 1)
        self.eixo1 = self.fig.add_subplot(self.gs[0])
        self.eixo2 = self.fig.add_subplot(self.gs[1])


    def adicionar(self, arquivo, m, tracejado):
        with open(arquivo) as ff:
            linhas = ff.readlines()
            T = [float(linha.split()[0]) for linha in linhas]
            X = [float(linha.split()[1]) for linha in linhas]
            Y = [float(linha.split()[2]) for linha in linhas]
        ff.close

        self.__configurarEixo(self.eixo1, 'Titulo do gráfico 1', T, X, tracejado, m, 'Eixo X')
        self.__configurarEixo(self.eixo2, 'Titulo do gráfico 2', T, Y, tracejado, m, 'Eixo Y')        
        
        
    def __configurarEixo(self, eixo, titulo, T, valores, tracejado, m, rotulo_y):
        eixo.set_title(titulo)
        eixo.plot(T, valores, tracejado, label='n = ' + str(m), color="black")
        eixo.set_ylabel(rotulo_y)
        eixo.set_xlabel('Eixo T')        
        eixo.legend()


    def mostrar(self):
        self.gs.tight_layout(self.fig)
        
#Fim da classe CONSTRUTORDEGRAFICO



#Classe SIMULADOR
class Simulador:
    
    def __init__(self, entrada):
        with open(entrada + '.txt') as f:
            self.x0 = float(f.readline())
            self.y0 = float(f.readline())
            self.t0 = float(f.readline())
            self.tf = float(f.readline())
            self.n = int(f.readline())
            self.m = int(f.readline())
        f.closed
        self.__simular()
        
        
    def __simular(self):
        self.__metodoDePassoUnicoBidimensional()
    
    
    def __metodoDePassoUnicoBidimensional(self):
        
        h = (self.tf - self.t0)/self.__calcularN()
        
        #Lista dos resultados com C.I. adicionada
        T = [self.t0]
        X = [self.x0]
        Y = [self.y0]

        with open(self.nomeArquivoDeSaida(), 'w+') as f:    
            
            for k in range(0, self.__calcularN()):
                t_k1 = T[k] + h
                x_k1 = X[k] + h * self.__fi(self.__eulerExplicito1(X[k], Y[k], T[k]))
                y_k1 = Y[k] + h * self.__fi(self.__eulerExplicito2(X[k], Y[k], T[k]))
                T.append(t_k1)
                X.append(x_k1)
                Y.append(y_k1)
                f.write(str(t_k1) + ' ' + str(x_k1) + ' ' + str(y_k1) + '\n')
            
        f.closed
            
            
    def __calcularN(self):
        return self.n*(2**self.m)
            
            
    def __fi(self, f):
        return f
        
        
    def __eulerExplicito1(self, x, y, t):
        return y
    
    
    def __eulerExplicito2(self, x, y, t):
        return -5*y + 4*x + math.sin(10*t)
        
    
    def nomeArquivoDeSaida(self):
        return 'saida_' + str(self.m) + '.txt'
#Fim da classe SIMULADOR
        
    
    
def main():
    
    sim2 = Simulador('entrada_2')
    sim3 = Simulador('entrada_3')
    sim4 = Simulador('entrada_4')

    construtorDeGrafico = ConstrutorDeGrafico()    
    construtorDeGrafico.adicionar(sim2.nomeArquivoDeSaida(), sim2.m, '--')
    construtorDeGrafico.adicionar(sim3.nomeArquivoDeSaida(), sim3.m, '-.')
    construtorDeGrafico.adicionar(sim4.nomeArquivoDeSaida(), sim4.m, ':')
    construtorDeGrafico.mostrar()
    
main()