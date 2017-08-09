#!/usr/bin/env python
import copy
minsupport = 4
C1={} 
#The dict {} in python such as:my_information = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
#name -> Pusheen the Cat (Key is name , value is Pusheen the cat)
def Apriori_gen(Itemset, k, lenght):
    canditate = []
    for i in range (0,lenght):

            element = str(Itemset[i])
            print element[0:(len(element)-1)]

file = open('example.txt')
for line in file:
    for item in line.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
C1.keys().sort()
C1.values().sort()
print C1.keys()
print C1.values()
#one_itemsets=copy.copy(C1.values())
#print one_itemsets
L1 = []
#L1 = set()
for i in C1:
    if C1[i] >= minsupport:
        L1.append(i)
L1.sort()
print L1
k=2
l = len(L1)
L2 = [ 'abc' , 'abe' ]
#L2 = Apriori_gen(L1, k ,l)
Apriori_gen(L2, k ,2)
