# -*- coding: utf-8 -*-

"""
Felipe Vasconcelos
8993027

Tarefa #01

Referencias: 
    - https://matplotlib.org/
    - https://docs.python.org/3/
"""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import math

#Classe CONSTRUTORDEGRAFICO
class ConstrutorDeGrafico:

    def __init__(self):
        self.fig = plt.figure()
        self.gs = gridspec.GridSpec(1, 1)
        self.eixo = self.fig.add_subplot(self.gs[0])


    def adicionar(self, arquivo, m, tracejado):
        with open(arquivo) as ff:
            linhas = ff.readlines()
            T = [float(linha.split()[0]) for linha in linhas]
            Y = [float(linha.split()[1]) for linha in linhas]
        ff.close
        self.__configurarEixo(self.eixo, 'Y X T', T, Y, tracejado, m, 'Y (admensional)')
        
        
    def __configurarEixo(self, eixo, titulo, T, valores, tracejado, m, rotulo_y):
        eixo.set_title(titulo)
        eixo.plot(T, valores, tracejado, label='m = ' + str(m), color="black")
        eixo.set_ylabel(rotulo_y)
        eixo.set_xlabel('T (admensional)')        
        eixo.legend()

    def adicionarSolucaoExata(self):
        with open('solucao_exata.txt') as ff:
            linhas = ff.readlines()
            Te = [float(linha.split()[0]) for linha in linhas]
            Ye = [float(linha.split()[1]) for linha in linhas]
        ff.close
        self.eixo.plot(Te, Ye, label='exata', color="black")
        self.eixo.legend()

    def mostrar(self):
        self.gs.tight_layout(self.fig)
#Fim da classe CONSTRUTORDEGRAFICO


#Classe SIMULADOR
class Simulador:
    
    def __init__(self, m):
        
        self.m = m
        with open('parametros_iniciais.txt') as f:
            self.t0 = float(f.readline())
            self.tf = float(f.readline())
            self.y0 = float(f.readline())            
            self.n = int(f.readline())

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
            return - math.sin(tk) + 2 * math.cos(tk) * math.sin(tk)
    
    def nomeArquivoDeSaida(self):
        return 'saida_' + str(self.m) + '.txt'
#Fim da classe SIMULADOR
        
    
#Classe GERADORDESOLUCAOEXATA
class GeradorDeSolucaoExata:
    
    def __init__(self):
        with open('parametros_iniciais.txt') as f:
            self.t0 = float(f.readline())
            self.tf = float(f.readline())
            self.y0 = float(f.readline())
            self.i = 2**10
        f.closed
        
        with open('solucao_exata.txt', 'w+') as f:   
            h = (self.tf - self.t0)/self.i
            t = self.t0

            for k in range(0, self.i+1):
                t_k1 = t + h * k
                y_k1 = self.__calcularSolucaoExata(t_k1)
                print(y_k1)
                f.write(str(t_k1) + ' ' + str(y_k1) + '\n')
        f.closed
        
    def __calcularSolucaoExata(self, tk):
        return math.cos(tk) + math.sin(tk)**2
#Fim da classe GERADORDESOLUCAOEXATA        
        
    
def main():
    
    sim_a = Simulador(1)
    sim_b = Simulador(2)
    sim_c = Simulador(3)
    
    construtorDeGrafico = ConstrutorDeGrafico()   
    
    construtorDeGrafico.adicionar(sim_a.nomeArquivoDeSaida(), sim_a.m, '--')
    #construtorDeGrafico.adicionar(sim_b.nomeArquivoDeSaida(), sim_b.m, '-.')
#  construtorDeGrafico.adicionar(sim_c.nomeArquivoDeSaida(), sim_c.m, ':')
    
    GeradorDeSolucaoExata()    
    construtorDeGrafico.adicionarSolucaoExata()
  
    construtorDeGrafico.mostrar()
    
main()