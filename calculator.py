'''
   Output from cProlife for original script

   1004015 function calls in 3.065 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    3.065    3.065 <string>:1(<module>)
        2    1.559    0.780    1.569    0.784 calculator.py:19(multiply)
        1    0.621    0.621    0.704    0.704 calculator.py:32(sqrt)
        1    0.000    0.000    3.063    3.063 calculator.py:45(hypotenuse)
        1    0.785    0.785    0.790    0.790 calculator.py:6(add)
  1000000    0.078    0.000    0.078    0.000 {math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {numpy.core.multiarray.zeros}
     4004    0.018    0.000    0.018    0.000 {range}

    We can see that the original code does poorly in {math.sqrt}
    There are too many loops in the functions, which leads to poor performance. 
    In order to speed up, I am going to replace those for loops by using numpy to return results of matrix operation directly

    After those change, the script speeds up from 3.065 seconds to 0.042 seconds
    
    7 function calls in 0.042 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.011    0.011    0.042    0.042 <string>:1(<module>)
        1    0.007    0.007    0.007    0.007 calculator.py:25(add)
        2    0.016    0.008    0.016    0.008 calculator.py:38(multiply)
        1    0.008    0.008    0.008    0.008 calculator.py:51(sqrt)
        1    0.000    0.000    0.030    0.030 calculator.py:64(hypotenuse)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    #m,n = x.shape
    #z = np.zeros((m,n))
    #for i in range(m):
    #    for j in range(n):
    #        z[i,j] = x[i,j] + y[i,j]
    return x+y


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    #m,n = x.shape
    #z = np.zeros((m,n))
    #for i in range(m):
    #    for j in range(n):
    #        z[i,j] = x[i,j] * y[i,j]
    return np.multiply(x,y)


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    #from math import sqrt
    #m,n = x.shape
    #z = np.zeros((m,n))
    #for i in range(m):
    #    for j in range(n):
    #        z[i,j] = sqrt(x[i,j])
    return np.sqrt(x)


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)