# -*- coding: utf-8 -*-

"""
Felipe Vasconcelos
8993027

Tarefa #02

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
        self.__configurarEixo(self.eixo, 'Euler Implícito: Y X T', T, Y, tracejado, m, 'Y (admensional)')
        
        
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
        self.__metodoDePassoUnico()
    
    
    def __metodoDePassoUnico(self):
        h = (self.tf - self.t0)/self.__calcularN()
        
        with open(self.nomeArquivoDeSaida(), 'w+') as f:    
        #Lista dos resultados com C.I. adicionada
            T = [self.t0]
            Y = [self.y0]
            f.write(str(self.t0) + ' ' + str(self.y0) + '\n')

        #Metodo Explicito
#            for k in range(0, self.__calcularN()):
#                t_k1 = T[k] + h
#                y_k1 = Y[k] + h * self.__fi(T[k], t_k1, Y[k], h)
#                T.append(t_k1)
#                Y.append(y_k1)
#                f.write(str(t_k1) + ' ' + str(y_k1) + '\n')

        #Metodo Implicito
            for k in range(0, self.__calcularN()):
                t_k1 = T[k] + h
                y_k1 = self.__eulerImplicito(T[k], t_k1, Y[k], h)
                T.append(t_k1)
                Y.append(y_k1)
                f.write(str(t_k1) + ' ' + str(y_k1) + '\n')
        f.closed
            
        
    def __calcularN(self):
        return self.n*(2**self.m)

    def nomeArquivoDeSaida(self):
        return 'saida_' + str(self.m) + '.txt'            
            
#    def __fi(self, tk, tk1, yk, h):
#        return self.__euler(tk, yk, h)
#        return self.__eulerModificado(tk, yk, h)
#        return self.__eulerAprimorado(tk, yk, h)


    #Metodos Implicitos
    def __eulerImplicito(self, tk, tk1, yk, h):
        chuteInicial = yk
        return self.__aproximarRaizPeloMetodoDeNewton(tk1, yk, chuteInicial, h)
    
    def __aproximarRaizPeloMetodoDeNewton(self, tk1, yk, chuteInicial, h):

        x0 = chuteInicial
        for k in range(0, 10):
            x = self.__metodoDeNewton(tk1, yk, x0, h)
            if(math.fabs(x - x0) < 0.0001):
                return x
            else:
                x0 = x
        
        print("O método falhou em encontrar a raiz com 10 iterações")


    def __metodoDeNewton(self, tk1, yk, yk1, h):
        return yk1 - self.__fDeNewton(tk1, yk, yk1, h)/self.__fLinhaDoNewton(h)
    
    def __fDeNewton(self, tk1, yk, yk1, h):
        return yk1 - yk - h * self.__yLinha(tk1, yk1)
        
    def __fLinhaDoNewton(self, h):
        return 1 - h
    
    
    #Metodos Explicitos
#    def __euler(self, tk, yk, h):
#        return self.__yLinha(tk, yk)
#        
#    def __eulerModificado(self, tk, yk, h):
#        return self.__yLinha(tk + h/2, yk + (h/2) * self.__yLinha(tk, yk))
#
#    def __eulerAprimorado(self, tk, yk, h):
#        return (1/2) * (self.__yLinha(tk, yk) + self.__yLinha(tk + h, yk + h * self.__yLinha(tk, yk)))
    

    def __yLinha(self, tk, yk):
        return yk - (5 * math.pi) * (math.e ** tk) * math.sin(5 * math.pi * tk) 
    
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
        return ( math.e ** tk ) * math.cos(5 * math.pi * tk)
#Fim da classe GERADORDESOLUCAOEXATA        
        
    
def main():
    
    sim_a = Simulador(1)
    sim_b = Simulador(2)
    sim_c = Simulador(3)
    sim_d = Simulador(4)
    sim_e = Simulador(5)
    sim_f = Simulador(6)
    sim_g = Simulador(7)
    sim_h = Simulador(8)
    sim_i = Simulador(9)
    sim_j = Simulador(10)
    
    construtorDeGrafico = ConstrutorDeGrafico()   
    
    construtorDeGrafico.adicionar(sim_c.nomeArquivoDeSaida(), sim_c.m, ':')
    construtorDeGrafico.adicionar(sim_f.nomeArquivoDeSaida(), sim_f.m, '-.')
    
    GeradorDeSolucaoExata()    
    construtorDeGrafico.adicionarSolucaoExata()
  
    construtorDeGrafico.mostrar()
    
main()