from mpi4py import MPI
import numpy as np
import unittest
from parallel_sorter import slice_data, get_value

class test_(unittest.TestCase):

	'''
	Test class for assignment 11 
	'''
	def set(self):
		pass

	def test_length(self): 
		self.assertTrue(len(slice_data(np.random.randint(0, 12, size = 12),4)) == 4)
		# test whether the length of slice_data output equal to size

if __name__ == '__main__':
	unittest.main()