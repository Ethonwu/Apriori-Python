#!/usr/bin/env python
import copy
minsupport = 4
C1={} #The dict {} in python such as:my_information = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
      #name -> Pusheen the Cat (Key is name , value is Pusheen the cat)
file = open('example.txt')
for line in file:
    for item in line.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
print C1.keys()
print C1.values()
#one_itemsets=copy.copy(C1.values())
#print one_itemsets
L1 = []
lenght = len(C1.keys())
for i in C1:
    if C1[i] >= minsupport:
        L1.append(i)
print L1


    
            



