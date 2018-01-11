# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,7,4,3,1,6,2,8]

plt.plot(x,y,':',label='scatter type')

x = [1,2,3,4,5,6,7,8]
y = [2,2,3,3,1,5,2,5]

plt.plot(x,y,'-.',label='scatter type')

x = [1,2,3,4,5,6,7,8]
y = [5,7,1,3,1,1,2,1]

plt.plot(x,y,'--',label='scatter type')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Titulo do gráfico')
plt.legend()
plt.show()
