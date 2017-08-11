#!/usr/bin/env python
import copy
minsupport = 3
C1={} 
file = open('example.txt')
#The dict {} in python such as:my_information = {'name': 'Pusheen the Cat', 'country': 'USA', 'favorite_numbers': [42, 105]}
#name -> Pusheen the Cat (Key is name , value is Pusheen the cat)
def Apriori_gen(Itemset, lenght):
    canditate = []
    canditate_index = 0
    for i in range (0,lenght):
        element = str(Itemset[i])
        for j in range (i+1,lenght):
            element1 = str(Itemset[j])
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
    return sorted(L)
def Apriori_count_subset(Canditate,Canditate_len):
    Lk = dict()
    file = open('example.txt')
    for l in file:
        l = str(l.split())
        print l
        for i in range (0,Canditate_len):
            key = str(Canditate[i])
            count = 0
            flag = True
            for k in key:
                #print k
                if k not in l:
                    flag = False
            if flag:
                count += 1
            Lk[key] = count
    file.close()
    print Lk

for line in file:
    for item in line.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
file.close()
C1.keys().sort()
L1 = []
L1 = Apriori_prune(C1,minsupport)
#print L1
k=2
test = []
test = Apriori_gen(L1,len(L1))
C2={}
print test
#C2 = Apriori_count_subset(test)
testlen = len(test)
Apriori_count_subset(test,testlen)
#print C2
