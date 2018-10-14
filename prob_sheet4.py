import numpy as np
import pylab as pl

points = 50

data_x = [a*np.pi/180 for a in np.linspace(0,360,points)]
data_y = np.sin(data_x)

print(data_x)
print(data_y)
pl.plot(data_x,data_y)



def interp(in_x):
    test_x = in_x
    msum = 0            
    for i in range(0,len(data_x)):
        data_copy = list(data_x)
        data_copy.pop(i)
        top = 1
        bot = 1
        for j in data_copy:
            top *= test_x - j
            bot *= data_x[i] - j
        
        msum += top*data_y[i]/bot
    
    out_y = msum
    print(out_y)
    return out_y


test = np.linspace(0,2*np.pi,10)
test_y = []
for a in test:
    test_y.append(interp(a))
    
pl.plot(test,test_y)



















