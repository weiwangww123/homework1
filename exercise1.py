# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:25:17 2022

@author: wwang3
"""

import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(0,2*np.pi,1000)
x1=2*np.cos(theta)+np.cos(2*theta)
y1=2*np.sin(theta)-np.sin(2*theta)
plt.plot(x1,y1,color='yellow')
plt.title("deltoid curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

x2=theta**2*np.cos(theta)
y2=theta**2*np.sin(theta)
plt.plot(x2,y2,color='blue')
plt.title("spiral curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

r=np.exp(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5
x3=r*np.cos(theta)
y3=r*np.sin(theta)
plt.plot(x3,y3,color='red')
plt.title("Fey's equation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()