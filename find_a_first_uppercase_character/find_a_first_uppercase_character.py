#Given a String, find a first uppercase character
#Solve both an iterative and recursive solution
input_str_1 = 'lucidProgramming'
input_str_2 = 'LucidProgramming'
input_str_3 = 'lucidprogramming'

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return 'No uppercase character found'

def find_recursive_recursion(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return 'No uppercase letter found.'
    
    return find_recursive_recursion(input_str, idx + 1)

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print('\n')
print(find_recursive_recursion(input_str_1))
print(find_recursive_recursion(input_str_2))
print(find_recursive_recursion(input_str_3))
