import matplotlib.pyplot as plt
import numpy as np
# NIS SCRIPT 
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(3*theta)
#create a polar plot 
plt.polar(theta, r)
plt.title("polar plot NiS")
plt.show()