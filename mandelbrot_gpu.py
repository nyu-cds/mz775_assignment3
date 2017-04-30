# 
# A CUDA version to calculate the Mandelbrot set
# Minqing Zhuang
# Apr 30 
#
from numba import cuda
import numpy as np
from pylab import imshow, show
import math

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters): 
    '''
    This function compute mandel by 
    1) getting initial coordinates of x and y
    2) computing the increment of index of x and y (x_step, y_step)
    3) finding the number of blocks in x and y direction (a, b)
    4) finding the starting and ending index for blocks (x_, y_)
    '''

    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    y_initial, x_initial = cuda.grid(2) # get the starting x, y coordinates

    # get the number of threads in y direction; also size for each block in x
    x_step = cuda.blockDim.y * cuda.gridDim.y 

    # get the number of threads in x direction; also size for each block in y 
    y_step = cuda.blockDim.x * cuda.gridDim.x 

    # partition data into blocks
    a = math.ceil(width/float(x_step)) 
    b = math.ceil(height/float(y_step))

    x_ = [x_step*i + x_initial for i in range(int(a))]
    y_ = [y_step*i + y_initial for i in range(int(b))]

    # compute mandel
    for x in x_:
        real = min_x + x * pixel_size_x
        for y in y_:
            imag = min_y + y * pixel_size_y
            if x < width and y < height:
                image[y, x] = mandel(real, imag, iters)


    
if __name__ == '__main__':
	image = np.zeros((1024, 1536), dtype = np.uint8)
	blockdim = (32, 8)
	griddim = (32, 16)
	
	image_global_mem = cuda.to_device(image)
	compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
	image_global_mem.copy_to_host()
	imshow(image)
	show()