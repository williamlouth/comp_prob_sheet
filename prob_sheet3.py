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
    

def Gaussian(A,b):
    for i in range(A.shape[1]):
        print("hiu")    
        print(A)
        
        
        A[1][i] = A[1][i]*A[0][0]/A[1][i] - A[0][i]
        b[1] = b[1]*A[0][0]/A[1][i] - b[0]
        
        A[2][i] = A[2][i]*A[0][0]/A[2][i] - A[0][i]
        b[2] = b[2]*A[0][0]/A[2][i] - b[0]
        
        print("here")
        A[0][i] = A[0][i]/A[0][0]
        b[0] = b[0]/A[0][0]

        #print(b[])
    
    return A,b



my_matrix = M_multiply(a,b)
print(my_matrix)
print(np.dot(a,b))




my_A = np.array([[5,6,77],[7,8,12],[1,2,65]])
my_b = np.array([[2],[5],[24]])
print(Gaussian(my_A,my_b))


















































