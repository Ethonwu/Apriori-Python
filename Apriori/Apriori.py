#!/usr/bin/env python
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

            



