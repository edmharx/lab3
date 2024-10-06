num_list = [1,2,3,4,5,6,7,8,9]

new_list = [num**2 for num in num_list if num%2 != 0]

print(new_list)