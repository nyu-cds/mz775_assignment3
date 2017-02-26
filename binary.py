"""
	Minqing Zhuang
	02/26/2017
    zbits function 
"""

import itertools as it

def zbits(n, k):
    '''
    The function takes two arguments n and k and prints all binary strings of length n that contain k zero bits
    '''
    
    binary_list = ''.join(str(i) for i in list(it.repeat(1,(n-k))) + list(it.repeat(0,k))) # create a binary list that consists of strings 1 and 0 
    permutations = list(it.permutations(binary_list, n)) # generate the permutation 
    reformat_permutations = [''.join(i for i in j) for j in permutations] # change format of permutation, for example change '1','1','0' to '110'
    return set(reformat_permutations) # use set to return unique results