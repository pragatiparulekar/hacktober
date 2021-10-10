# https://www.geeksforgeeks.org/comprehensions-in-python/


# Using List comprehensions 
# for constructing output list 

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7] 


# list_using_comp = [var for var in input_list if var % 2 == 0] 
# list_using_squre = [var**2 for var in range(1, 10)] 

# print("Output List using list comprehensions:", list_using_comp) 
# print("Output List using list comprehensions:", list_using_squre) 


# Using Dictionary comprehensions 
# for constructing output dictionary 

input_list = [1,2,3,4,5,6,7] 

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0} 

print("Output Dictionary using dictionary comprehensions:", dict_using_comp) 


# Using Set comprehensions 
# for constructing output set 

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] 

set_using_comp = {var for var in input_list if var % 2 == 0} 

print("Output Set using set comprehensions:", set_using_comp) 


# generator comprehension:
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7] 

output_gen = (var for var in input_list if var % 2 == 0) 

print("Output values using generator comprehensions:", end = ' ') 

for var in output_gen: 
	print(var, end = ' ') 
