# -*- coding: utf-8 -*-

"""
Felipe Vasconcelos
8993027

Tarefa #10

Referencias:
    - https://matplotlib.org/
    - https://docs.python.org/3/
    - https://rosettacode.org/wiki/Runge-Kutta_method#Alternate_solution
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
            Y1 = [float(linha.split()[1]) for linha in linhas]
            Y2 = [float(linha.split()[2]) for linha in linhas]
            Y3 = [float(linha.split()[3]) for linha in linhas]
            Y4 = [float(linha.split()[4]) for linha in linhas]
        ff.close
        
        #TROCAR PARA IMPRIMIR UM GRAFICO POR VEZ. SINCRONIZAR COM SOLUCAO EXATA
        self.__configurarEixo(self.eixo, 'Y1 X T', T, Y1, tracejado, m, 'Y1 (admensional)')
#        self.__configurarEixo(self.eixo, 'Y2 X T', T, Y2, tracejado, m, 'Y2 (admensional)')
#        self.__configurarEixo(self.eixo, 'Y3 X T', T, Y3, tracejado, m, 'Y3 (admensional)')
#        self.__configurarEixo(self.eixo, 'Y4 X T', T, Y4, tracejado, m, 'Y4 (admensional)')

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
            self.y1_0 = float(f.readline())
            self.y2_0 = float(f.readline())
            self.y3_0 = float(f.readline())
            self.y4_0 = float(f.readline())
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
            Y1 = [self.y1_0]
            Y2 = [self.y2_0]
            Y3 = [self.y3_0]
            Y4 = [self.y4_0]
            f.write(str(self.t0) + ' ' + str(self.y1_0) + ' ' + str(self.y2_0) + ' ' + str(self.y3_0) + ' ' + str(self.y4_0) +   '\n')

        #Metodo Explicito
            for i in range(0, self.__calcularN()):
               tk = T[i]
               t_k1 = tk + h
               T.append(t_k1)

               y1_k = Y1[i] 
               y2_k = Y2[i] 
               y3_k = Y3[i] 
               y4_k = Y4[i] 
               
               y1_k1 = y1_k + self.__fi(self.__y1Linha, tk, h, y1_k, y2_k, y3_k, y4_k)
               y2_k1 = y2_k + self.__fi(self.__y2Linha, tk, h, y1_k, y2_k, y3_k, y4_k)
               y3_k1 = y3_k + self.__fi(self.__y3Linha, tk, h, y1_k, y2_k, y3_k, y4_k)
               y4_k1 = y4_k + self.__fi(self.__y4Linha, tk, h, y1_k, y2_k, y3_k, y4_k)
               
               Y1.append(y1_k1)
               Y2.append(y2_k1)
               Y3.append(y3_k1)
               Y4.append(y4_k1)
               
               f.write(str(t_k1) + ' ' + str(y1_k1) + ' ' + str(y2_k1) + ' ' + str(y3_k1) + ' ' + str(y4_k1) + '\n')
              
        f.closed

    def __calcularN(self):
        return self.n*(2**self.m)

    def nomeArquivoDeSaida(self):
        return 'saida_' + str(self.m) + '.txt'

    def __fi(self, ylinha, tk, h, y1_k, y2_k, y3_k, y4_k):
        return self.__rungeKuttaTerceiraOrdem(ylinha, tk, h, y1_k, y2_k, y3_k, y4_k)

    def __rungeKuttaTerceiraOrdem(self, ylinha, tk, h, y1_k, y2_k, y3_k, y4_k):
        k1 = h * ylinha(tk, y1_k, y2_k, y3_k, y4_k)
        
        k2_fator = (k1/2)
        k2 = h * ylinha(tk + h/2, y1_k + k2_fator, y2_k + k2_fator, y3_k + k2_fator, y4_k + k2_fator)
        
        k3_fator = - k1 + (2*k2)
        k3 = h * ylinha(tk + h, y1_k + k3_fator, y2_k + k3_fator, y3_k + k3_fator, y4_k + k3_fator)
        
        return (k1 + 4 * k2 + k3)/6
    
    def __y1Linha(self, tk, y1_k, y2_k, y3_k, y4_k):
        return 1 * y1_k

    def __y2Linha(self, tk, y1_k, y2_k, y3_k, y4_k):
        return 2 * y2_k

    def __y3Linha(self, tk, y1_k, y2_k, y3_k, y4_k):
        return 3 * y3_k
    
    def __y4Linha(self, tk, y1_k, y2_k, y3_k, y4_k):
        return 4 * y4_k
    
#Fim da classe SIMULADOR


#Classe GERADORDESOLUCAOEXATA
class GeradorDeSolucaoExata:

    def __init__(self):
        with open('parametros_iniciais.txt') as f:
            self.t0 = float(f.readline())
            self.tf = float(f.readline())
            self.i = 2**10
        f.closed

        with open('solucao_exata.txt', 'w+') as f:
            h = (self.tf - self.t0)/self.i
            t = self.t0

            for k in range(0, self.i+1):
                t_k1 = t + h * k
                y_k1 = self.__calcularSolucaoExata1(t_k1)
#                y_k1 = self.__calcularSolucaoExata2(t_k1)
#                y_k1 = self.__calcularSolucaoExata3(t_k1)
#                y_k1 = self.__calcularSolucaoExata4(t_k1)

                f.write(str(t_k1) + ' ' + str(y_k1) + '\n')
        f.closed

    def __calcularSolucaoExata1(self, tk):
        return ( math.e ** (1*tk) )

    def __calcularSolucaoExata2(self, tk):
        return ( math.e ** (2*tk) )

    def __calcularSolucaoExata3(self, tk):
        return ( math.e ** (3*tk) )

    def __calcularSolucaoExata4(self, tk):
        return ( math.e ** (4*tk) )
    
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

    construtorDeGrafico.adicionar(sim_a.nomeArquivoDeSaida(), sim_a.m, ':')
    construtorDeGrafico.adicionar(sim_c.nomeArquivoDeSaida(), sim_c.m, '-.')

    GeradorDeSolucaoExata()
    construtorDeGrafico.adicionarSolucaoExata()

    construtorDeGrafico.mostrar()

main()
