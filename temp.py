# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]


plt.plot(x,y,label='Primeira linha')
plt.plot(x2,y2,label='Segunda linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Titulo do gráfico')
plt.legend()
plt.show()
