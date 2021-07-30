# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:01:11 2021

@author: user
"""

# Q1
input = [17,19,5,4,3,1]

def max_of_right(array):
    ans = []
    for i in range(1,len(array)):
        ans.append(max(array[i:]))
    
    ans.append(-1)
    return ans

ans = max_of_right(input)


# Q2
input = ['====','@---@']

def letter_returner(strings_list):
    
    for i in range(1,len(strings_list)):
        
        strings_list[i] = strings_list[i].lower()
    
    ans = 'set()'
    tmp = set(strings_list[0])
    
    for i in range(1,len(strings_list)):      
        tmp = tmp.intersection(set(strings_list[i]))
    
    if len(tmp) > 0:
        ans = tmp
        return ans
    else:
        return ans
    
print(letter_returner(input))
    
    

# Q3
input = [8,9,2,2,5]

def drop_duplicate_and_compute_average(input_array):
    tmp = list(set(input))
    ans = sum(tmp)/len(tmp)
    return ans

print(drop_duplicate_and_compute_average(input))











    
    
    
    
