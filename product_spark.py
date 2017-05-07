'''
Minqing Zhuang

Assignment 13

May 7, 2017
'''

from pyspark import SparkContext
from operator import mul

sc = SparkContext('local','product')
print('The product is '+str(sc.parallelize(range(1, 1001)).fold(1,mul))) # get the product of all number using fold