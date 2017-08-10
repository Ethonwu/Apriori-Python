#!/usr/bin/env python
import copy
minsupport = 3
C1={} 
file = open('example.txt')
#The dict {} in python such as:my_information = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
#name -> Pusheen the Cat (Key is name , value is Pusheen the cat)
def Apriori_gen(Itemset, k, lenght):
    canditate = []
    canditate_index = 0
    for i in range (0,lenght):
        element = str(Itemset[i])
        for j in range (i+1,lenght):
            element1 = str(Itemset[j])
            #print element[0:(len(element)-1)]
            if element[0:(len(element)-1)] == element1[0:(len(element1)-1)]:
                    unionset = element[0:(len(element)-1)]+element1[len(element1)-1]+element[len(element)-1] #Combine (k-1)-Itemset to k-Itemset 
                    unionset = ''.join(sorted(unionset))  #Sort itemset by dict order
                    canditate.append(unionset)
    return canditate
def Apriori_prune(Ck,MinSupport):
    L = []
    for i in Ck:
        if Ck[i] >= minsupport:
            L.append(i)
    L = sorted(L)
    return L
for line in file:
    for item in line.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
C1.keys().sort()
L1 = []
L1 = Apriori_prune(C1,minsupport)
print L1
k=2
test = []
test = Apriori_gen(L1, k ,len(L1))
print test
