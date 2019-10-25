import numpy as np  # numpy lib we called
import matplotlib.pyplot as plt # for plot we need this library

x=np.linspace(0,2*np.pi,50) #this is my array
y=np.sin(x) #depens on x  , my y array
z=np.cos(x) # my z array for depend x value





plt.plot(x,y,'b-d' ,linewidth=2,label='sinx') # line describe blue colar means b d shape describe
plt.plot(x,z,'r-o' ,linewidth=2,label='cosx') # line describe red means r also shape o describe 
plt.grid(True) #grid for background
plt.axis([0,2*np.pi,-1.5,1.5]) #plot axis range
plt.title('Sine & Cosine Waves') #title of graph
plt.xlabel('Time in Seconds') #x axis name
plt.ylabel('Waves')  #y axis name
plt.legend() #show the legent 
plt.show() #shown graph not enough plot if you dont write this
    
