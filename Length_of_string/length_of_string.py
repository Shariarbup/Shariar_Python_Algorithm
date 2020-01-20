#Given a String. Calculate the lengrh of the String.
input_str = 'Lucidprogramming'
print(len(input_str))

def iterative_str_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def recursive_str_len(input_str, idx = 0):
    count = 0
    if idx != len(input_str) - 1:
        count += 1
    if idx == len(input_str) - 1:
        return count
    return recursive_str_len(input_str, idx + 1)

print("Iterative way to find String length : ",iterative_str_len(input_str))
print('\n')
print("Recursive way to find String length : ",recursive_str_len(input_str))
