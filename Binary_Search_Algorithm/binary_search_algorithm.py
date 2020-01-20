data = [2, 3, 4, 23, 34, 45, 28, 12, 34, 67]
target = 28
#Linear_Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
#Binary_search_iterative
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#Recursive_binary_search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high) 
    


print('Linear Search : ',linear_search(data, target))
print('Binary Search Iterative : ',binary_search_iterative(data, target))
print('Binary Search Recursive : ',binary_search_recursive(data, target, 0, len(data)-1))
