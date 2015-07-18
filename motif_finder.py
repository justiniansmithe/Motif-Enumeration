'''
Code by Justin Smith written for rosalind.info
Solves the Motiff Enumeration Problem with python2.7

from rosalind:
---------------------------------------------------------
Implanted Motif Problem
Find all (k, d)-motifs in a collection of strings.

Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.
---------------------------------------------------------
'''


import itertools
from collections import Counter
import copy

dataset = open('rosalind_motiff_sample.txt', 'r')

#ATTTGGC
#TGCCTTA
#CGGTATC
#GAAAATT

data=[]
for line in dataset:
	data.append(line.strip())

#print data
k= 5
d = 1

t = [p for p in itertools.product('ACTG', repeat=k)]

listOfPerms=[]

for i in t:
	listOfPerms.append(''.join(i)) 

print data
# data = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']

kmers = []
line_list = []
def findKmersSet(k, stuff):
	i=0
	for line in data:
		line_list = []
		for i in range(0,int(len(line)-k+1)):
			line_list.append(line[i:i+k])
		kmers.append(line_list)
	

def hamming(str1, str2):
	diffs= 0
	for char1, char2 in zip(str1, str2):
		if char1 != char2:
				diffs += 1
	return diffs

findKmersSet(5, data)

candidate_list = []

def motif():
	for perm in listOfPerms:
		print  '\n' + perm
		for item in kmers:
			print ''

			truthValues = []

			for i in item:
				print hamming(i, perm),
				print i,
				if hamming(i, perm) <= d:
					truthValues.append(True)
					print 'true',
				else:
					truthValues.append(False)
					print 'false',
			if any(truthValues):
				#candidate_list.append(perm)
				continue
			else:
				break
		if any(truthValues):
			candidate_list.append(perm)

			print truthValues
					


print kmers
print len(kmers)
motif()
print '\n'
print candidate_list

for i in candidate_list:
	print i,
