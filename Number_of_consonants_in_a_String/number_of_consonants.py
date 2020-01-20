# Given a String. Count the number of consonants
# Note consonant is a letter, that is not a vowel.
# i.e. a letter that is not a, e, i,  o, or u.

input_str_1 = 'abc de'
input_str_2 = 'LucidPrograMminG'
vowels = 'aeiou'

def iterative_count_consonants(input_str):
    count = 0
    for i in range (len(input_str)):
        if input_str[i] not in vowels and input_str[i].isalpha():
            count += 1
    return count
def recursive_count_consonants(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])

print('Iterative way to count consonants : ',iterative_count_consonants(input_str_1))
print('Iterative way to count consonants : ',iterative_count_consonants(input_str_2))
print('\n')
print('Recursive way to count consonants :',recursive_count_consonants(input_str_1))
print('Recursive way to count consonants :',recursive_count_consonants(input_str_2))
