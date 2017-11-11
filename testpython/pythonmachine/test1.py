import matplotlib.pyplot as plt
import numpy as np
import math

#Each point on the generating curve
x = np.arange(-3,3,0.1)

def least_square_color1(y,order,error_x,error_y):
    #The offset of each point on the generated curve
    i=0
    xa=[]
    ya=[]
    for xx in x:
        yy=y[i]
        d_x=np.random.normal(0,error_x)
        d_y=np.random.normal(0,error_y)
        i+=1
        xa.append(xx+d_x)
        ya.append(yy+d_y)

    plt.plot(xa,ya,color='m',linestyle='',marker='.')

    #Curve fitting
    matA=[]
    for i in range(0,order+1+1):
        matA1=[]
        for j in range(0,order+1+1):
            tx=0.0
            for k in range(0,len(xa)):
                dx=1.0
                for l in range(0,j+i):
                    dx=dx*xa[k]
                tx+=dx
            matA1.append(tx)
        matA.append(matA1)
    matA=np.array(matA)

    matB=[]
    for i in range(0,order+1+1):
        ty=0.0
        for k in range(0,len(xa)):
            dy=1.0
            for l in range(0,i):
                dy=dy*xa[k]
            ty+=ya[k]*dy
        matB.append(ty)
    matB=np.array(matB)

    matAA=np.linalg.solve(matA,matB)

    #Draw the curve fitting
    xxa= np.arange(-3,3,0.01)
    yya=[]
    for i in range(0,len(xxa)):
        yy=0.0
        for j in range(0,order+1+1):
            dy=1.0
            for k in range(0,j):
                dy*=xxa[i]
            dy*=matAA[j]
            yy+=dy
        yya.append(yy)
    plt.plot(xxa,yya,color='r',linestyle='-',marker='')

def least_square_color2(y,order,error_x,error_y):
    #The offset of each point on the generated curve
    i=0
    xa=[]
    ya=[]
    for xx in x:
        yy=y[i]
        d_x=np.random.normal(0,error_x)
        d_y=np.random.normal(0,error_y)
        i+=1
        xa.append(xx+d_x)
        ya.append(yy+d_y)

    plt.plot(xa,ya,color='b',linestyle='',marker='.')

    #Curve fitting
    matA=[]
    for i in range(0,order+1+1):
        matA1=[]
        for j in range(0,order+1+1):
            tx=0.0
            for k in range(0,len(xa)):
                dx=1.0
                for l in range(0,j+i):
                    dx=dx*xa[k]
                tx+=dx
            matA1.append(tx)
        matA.append(matA1)
    matA=np.array(matA)

    matB=[]
    for i in range(0,order+1+1):
        ty=0.0
        for k in range(0,len(xa)):
            dy=1.0
            for l in range(0,i):
                dy=dy*xa[k]
            ty+=ya[k]*dy
        matB.append(ty)
    matB=np.array(matB)

    matAA=np.linalg.solve(matA,matB)

    #Draw the curve fitting
    xxa= np.arange(-3,3,0.01)
    yya=[]
    for i in range(0,len(xxa)):
        yy=0.0
        for j in range(0,order+1+1):
            dy=1.0
            for k in range(0,j):
                dy*=xxa[i]
            dy*=matAA[j]
            yy+=dy
        yya.append(yy)
    plt.plot(xxa,yya,color='g',linestyle='-',marker='')

order=[1,2,3]
error_y=1
error_x_mat=[0.1,0.2]
'''
x with noise 0~0.1: pink dots, red lines
x with noise 0~0.2: blue dots, green lines
'''
for order in range(len(order)):
    for error_x in error_x_mat:

        plt.subplot(330+order+1)
        plt.ylabel('order={}'.format(order+1))
        plt.title('y=2x+1',fontsize=10)
        y = [2*a+1 for a in x]
        if error_x==0.1:
            least_square_color1(y,order,error_x,error_y)
        else:
            least_square_color2(y,order,error_x,error_y)

        plt.subplot(333+order+1)
        plt.ylabel('order={}'.format(order+1))
        plt.title('$y=0.01x^{2}+2x+1$',fontsize=10)
        y = [0.01*a*a+2*a+1 for a in x]
        if error_x==0.1:
            least_square_color1(y,order,error_x,error_y)
        else:
            least_square_color2(y,order,error_x,error_y)

        plt.subplot(336+order+1)
        plt.ylabel('order={}'.format(order+1))
        plt.title('$y=0.1e^{0.1x}+2x+1$',fontsize=10)
        y = [0.1*(math.e**(0.1*a))+2*a+1 for a in x]
        if error_x==0.1:
            least_square_color1(y,order,error_x,error_y)
        else:
            least_square_color2(y,order,error_x,error_y)

plt.legend()
plt.show()