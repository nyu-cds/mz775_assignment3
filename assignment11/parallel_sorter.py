'''
Assignment 11

Minqing Zhuang

Apr 23
'''

from mpi4py import MPI
import numpy as np


def get_value():
	'''
	Get value of the number of integers from users.
	This number will also be the maximum integer of the random integer list
	'''
	while True:
		try:
		    num = int(raw_input('Please enter the number of integers: '))
		except ValueError:
		    continue
		break
	return num 


def slice_data(raw_list,size):
	'''
	Function that slices a list into bins by values
	'''
	cutoff = [(max(raw_list)/float(size))*float(i) for i in range(size+1)] 
	cutoff[-1] = max(raw_list) + 1
	#cutoff values for arrange integers into bins; length should be size+1

	bin_list = [raw_list[np.where((raw_list >= cutoff[i]) & (raw_list < cutoff[i+1]))] for i in range(len(cutoff)-1)] 
	#slice the raw list into bins by values

	return bin_list


if __name__ == '__main__':

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	if rank == 0:
		num = get_value()
		raw_list = np.random.randint(0,high = num, size = num) # initialize list with random integers
		bin_list = slice_data(raw_list,size)
	else:
		bin_list = None

	scattered_data = comm.scatter(bin_list,root=0) # scatter data to processes
	scattered_data.sort() # sort data
	collected_data = comm.gather(scattered_data, root=0) # collect data

	if rank == 0:
		print np.concatenate(collected_data) # print sorted list 


