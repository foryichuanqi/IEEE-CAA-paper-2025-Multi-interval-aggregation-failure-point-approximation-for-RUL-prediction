# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:53:32 2023

@author: Administrator
"""

a=1
c=10

for b in range(2,10):
    
    # print(b)
    sum_b=0
    for x in range(2,b):
        # print(x)
        # print(b)
        sum_b+=(x)
        # print(sum_b)
        
    for x in range(b,10,1):
        # print(x)
        
        sum_b+=int(x/b)
        # print(x - int(x/b) *b)
        
        # sum_b+=x - int(x/b) *b
        
        sum_b+=x%b
        
    print(b)
    print(sum_b)
    
    print( "    ")
    
        
# for x in range(2,2):
#     print(x)        

# a=1
# c=10

# for b in range(2,10):
    
#     # print(b)
#     sum_b=0
#     for x in range(2,b):
#         print(x)
#         print(b)
#         sum_b+=(x)
#         # print(sum_b)