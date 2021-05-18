import matplotlib
from tkinter import *
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

xVars = [1,2,3,4]
yVars = [1,2,3,4]
yVars2 = [1,3,6,9]
plt.plot(xVars, yVars, 'b-', label = "something")
plt.plot(xVars, yVars2, 'r--', label = '"something2"')

plt.show()