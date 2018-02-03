# -*- coding: utf-8 -*-

"""
Felipe Vasconcelos
8993027

Tarefa #01

Referencias: 
    - https://matplotlib.org/
    - https://docs.python.org/3/
"""

import matplotlib.pyplot as plt
import math

#Classe CONSTRUTORDEGRAFICO
class ConstrutorDeGrafico:

    def __init__(self):
        self.fig = plt.figure()


    def adicionar(self, arquivo, m, tracejado):
        with open(arquivo) as ff:
            linhas = ff.readlines()
            T = [float(linha.split()[0]) for linha in linhas]
            Y = [float(linha.split()[1]) for linha in linhas]
        ff.close
        self.__configurarEixo('Y X T', T, Y, tracejado, m, 'Y (admensional)')        
        
        
    def __configurarEixo(self, titulo, T, valores, tracejado, m, rotulo_y):
        plt.title(titulo)
        plt.plot(T, valores, tracejado, label='m = ' + str(m), color="black")
        plt.set_ylabel(rotulo_y)
        plt.set_xlabel('T (admensional)')        
        plt.legend()


    def mostrar(self):
        plt.show()
#Fim da classe CONSTRUTORDEGRAFICO



#Classe SIMULADOR
class Simulador:
    
    def __init__(self, entrada):
        with open(entrada + '.txt') as f:
            
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
        Y = [self.y0]

        with open(self.nomeArquivoDeSaida(), 'w+') as f:    
            for k in range(0, self.__calcularN()):
                t_k1 = T[k] + h
                y_k1 = Y[k] + h * self.__fi(T[k], Y[k], h)
                T.append(t_k1)
                Y.append(y_k1)
                f.write(str(t_k1) + ' ' + str(y_k1) + '\n')
        f.closed
            
            
    def __calcularN(self):
        return self.n*(2**self.m)
            
            
    def __fi(self, tk, yk, h):
        #return self.__eulerModificado(tk, yk, h)
        return self.__eulerModificado(tk, yk, h)
        #return self.__eulerAprimorado(tk, yk, h)


    def __euler(self, tk, yk, h):
        return self.__yLinha(tk, yk)
        
    def __eulerModificado(self, tk, yk, h):
        return self.__yLinha(tk + h/2, yk + (h/2) * self.__yLinha(tk, yk))

    def __eulerAprimorado(self, tk, yk, h):
        return (1/2) * (self.__yLinha(tk, yk) + self.__yLinha(tk + h, yk + h * self.__yLinha(tk, yk)))
        

    def __yLinha(self, tk, yk):
            return - math.sin(tk) + math.cos(tk)
    
    def nomeArquivoDeSaida(self):
        return 'saida_' + str(self.m) + '.txt'
#Fim da classe SIMULADOR
        
    
    
def main():
    
    sim_a = Simulador('entrada_1')
    sim_b = Simulador('entrada_3')
   # sim_c = Simulador('entrada_7')

    construtorDeGrafico = ConstrutorDeGrafico()    
    construtorDeGrafico.adicionar(sim_a.nomeArquivoDeSaida(), sim_a.m, '--')
    construtorDeGrafico.adicionar(sim_b.nomeArquivoDeSaida(), sim_b.m, '-.')
  #  construtorDeGrafico.adicionar(sim_c.nomeArquivoDeSaida(), sim_c.m, ':')
    construtorDeGrafico.mostrar()
    
main()