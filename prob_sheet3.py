import numpy as np


a = np.array([[1,2],[3,4],[5,9]])

b = np.array([[5,6,77],[7,8,12]])



def M_multiply(a,b):
    c = np.zeros((a.shape[0],b.shape[1]))
    
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            num = 0
            for k in range(a.shape[1]):
                num += a[i][k]*b[k][j]

            c[i][j] = num
    
    
    return c;
    


my_matrix = M_multiply(a,b)
print(my_matrix)
print(np.dot(a,b))


















































