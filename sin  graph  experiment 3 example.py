import numpy as np  # numpy lib we called
import matplotlib.pyplot as plt # for plot we need this library

x=[] #we define x
y=[]  # we define y


for i in np.arange(0,2*np.pi,2*np.pi/1000):  #try to draw sin graph
    x.append(i) # i x values
    y.append(np.sin(i)) #when we put x values we will get y values


plt.plot(x,y,'b-' ,linewidth=2) # line describe 
plt.grid(True) #grid for background
plt.axis([0,2*np.pi,-1.5,1.5]) #plot axis
plt.title('Sine Wave') #title of graph
plt.xlabel('Time in Seconds') #x axis name
plt.ylabel('Sin(t)')  #y axis name
plt.show() #shown graph not enough plot if you dont write this
    
