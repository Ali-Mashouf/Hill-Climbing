import numpy as np
import random
import matplotlib.pyplot as plt

def func(x, y):   
    #return np.sin(np.sqrt(x**2 + y**2))
    return -x**2 - y**2 + 4

current_x = random.uniform(-10, 10)  
current_y = random.uniform(-10, 10)
current_z = func(current_x, current_y)  

iterations = 1000  
step_size = 0.1    


for i in range(iterations):  
    
    new_x = current_x + random.uniform(-step_size, step_size)
    new_y = current_y + random.uniform(-step_size, step_size)
    new_z = func(new_x, new_y)
    
    if new_z > current_z:     
        current_x, current_y, current_z = new_x, new_y, new_z
print('The best point found by the algorithm :')
print('x = {} va y = {} va z = {}'.format(current_x, current_y, current_z))

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)
z = func(x, y)

fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', alpha = 0.5)
 
ax.scatter(current_x, current_y, current_z, color='r', s=100)
plt.show()
