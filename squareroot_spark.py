'''
Minqing Zhuang

Assignment 13

May 7, 2017
'''

from pyspark import SparkContext
from operator import add
import math

sc = SparkContext('local','squareroot')
squareroots = sc.parallelize(range(1, 1001)).map(math.sqrt) # get the squareroots of all numbers by using map 
print('The average is ' + str(squareroots.fold(0,add)/float(1000))) # sum the squareroots using fold, then the sum is divided by 1000