'''
Minqing Zhuang

Assignment 13

May 7, 2017
'''


from pyspark import SparkContext
from operator import add
import re

#
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    line = line.encode('ascii','ignore') 
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "distinct_words")
	
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	words_mapped = words.map(lambda x: (x,1))

	print('The number of distinct words in the input file is '+ str(words_mapped.keys().distinct().count())) # get the number of distinct words
