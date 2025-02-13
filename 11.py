# linear Search: works on brute force algorithm
def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
        
    return -1


l = [1,2,3,4,5]
print(linear_search(l,6));
print(sum())


# Time complexity of linear Search is O(n)
# Sorting is not required

