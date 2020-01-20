"""
problem: Give some integer N. Determine the Nth term in the look and say sequence.
Example: N = 4, the 4th term in the sequence is 1211.
1
11
21
1211
111221

"""
def next_number(s):
    result = []
    i =  0
    while i < len(s):
        count =  1
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = '1211'
print(next_number(s))

print('\nLook and Say sequence:')
ss = '1'
n = 5
print(1)
for i in range(n - 1):
    ss = next_number(ss)
    print(ss)
