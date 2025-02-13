# how to detect an array is sorted or not 

import random as r #this is for Monkey Sort
import time as time #this is for Monkey Sort

def isSorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            sorted = False
            print(sorted)
            return sorted
    print(sorted)
    return sorted

# Monkey Sort

def Monkey(arr):\

    while not isSorted(arr):
        time.sleep(1)
        r.shuffle(arr)
        print(arr)
    return arr


def bubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = 0 #to make it adaptive
        # print(i)
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if flag == 0 : #to make it adaptive
            break
    
    return arr


def SelectionSort(arr):
    if not isSorted(arr):
        for i in range(len(arr) - 1):
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
                    # print(min)
            arr[i],arr[min] = arr[min],arr[i]
        return arr
    
def merge(arr1,arr2): #if 2 sorted arrays are provided this function will merge the two arrays and return a sorted array
    i = 0             #it can be optimised by making the changes in the array itself it is in the video: 11:37:00
    j = 0
    merge = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1
    

    while i < len(arr1):
        merge.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        merge.append(arr2[j])
        j+=1
    
    return merge
        

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left,right)
        


# arr = [1,2,3,4,5,-1]
 
# print(isSorted(arr))

# arr = [5,7,-1,0,1]

# arr = Monkey(arr)

# print(arr)

# print(bubbleSort(arr))
# print(arr)

# print(SelectionSort(arr))


# -------------------bubble sort vs selection sort----------------
# l=[]
# for i in range(0,10000):
#     l.append(r.randint(0,10000))

# # print(l)
# l1 = l[:]
# start = time.time()
# bubbleSort(l)
# end = time.time()
# print(end- start, " for bubble sort")

# start = time.time()
# SelectionSort(l)
# end = time.time()
# print(end - start, " for selection sort")


# Merge Sort

print(mergeSort([7,4,8,-1,65,874,5584,-555,-4,0]))