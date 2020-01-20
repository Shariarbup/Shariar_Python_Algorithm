# Given two numbers. Find their product using recursion.
# 5 x 3
# 5 + 5 + 5
#recursion
# (x=5, y=3)
# 5 + (5, 2)
# 5 + (5, 1)
# 5 + (5, 0)

x = 55
y = 3000

def recursive_multiply(x, y):
    # This cuts down the total number of 
    # recursive calls
    # y must be less than the x in recursive multiplication
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    else:
        return x + recursive_multiply(x, y - 1)
print(x * y)
print('Recursive way to multiply two numbers : ',recursive_multiply(x, y))
