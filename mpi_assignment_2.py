from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

randNum = np.zeros(1)

def get_value_from_user():
	while True:
	    try:
	        value = int(raw_input('Please enter an integer less than 100: '))
	        if value >= 100: 
				print('Integer is larger than 100. Please make sure it is less than 100')
				continue
	    	else:
	    		break
	    except ValueError:
	        print('Value is not an integer. Please enter again and make sure it is integer')
	        continue
	return value	


if rank == 0:
	value = get_value_from_user()
	randNum[0] = value
	comm.Send(randNum, dest=1)
	comm.Recv(randNum, source=size-1)
	print ('Process '+str(size-1)+' send value '+str(randNum[0])+' back to process 0')

elif rank == (size-1):
	comm.Recv(randNum, source=rank-1)
	randNum = randNum*rank
	comm.Send(randNum, dest=0)


elif 0<rank<(size-1):
	comm.Recv(randNum, source=rank-1)
	randNum = randNum*rank
	comm.Send(randNum, dest=rank+1)
