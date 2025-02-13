# Binary Search: requires sorted array
# Time complexity is O(logn)


# using loop
def binarySearch(arr,val):
    low = 0
    high = len(arr) - 1
    while True:
        mid = (low+high)//2
        if(arr[mid] == val):
            return mid
        elif val > arr[mid]:
            low = mid +1
        elif val < arr[mid]:
            high = mid -1
        if low > high:
            return "Item not found"

# using recursion
def binarySearchRecursion(arr,low,high,val ):
    if low > high:
        return -1
    else:
        mid = (low+high)//2 
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            return binarySearchRecursion(arr,mid+1,high,val)
        else:
            return binarySearchRecursion(arr,low,mid-1,val)

l = [i for i in range(10)]
# print(binarySearch(l,10));
print(binarySearchRecursion(l,0,len(l)-1,5));