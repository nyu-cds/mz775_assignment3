from mpi4py import MPI

#create comm object and get rank for process
rank = MPI.COMM_WORLD.Get_rank()

# if it is even rank
if rank%2 == 0:
	print('Hello from even rank '+str(rank))

# if it is odd rank
else:
	print('Goodbye from odd rank '+str(rank))