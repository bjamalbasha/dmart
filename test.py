# -*- coding: cp1252 -*-
#config.py:
    #a=0
    #b=0
    #c=0

#module1.py:
    #import config 
    #config.a = 1
    #config.b =2
    #config.c=3
#print “ a, b & resp. are : “ , config.a, config.b, config.c


l1=[1,2,3]
l2=[2,3,4]
a=[l1[i]+l2[i]  for i in range(len(l1))]
print a
