import math
'''
// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
'''

def binary_search(nums, value):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = math.floor((left + right) / 2)
        print(f"i:{mid} nums[{mid}] --> {nums[mid]}")
        if nums[mid] < value:
            left = mid + 1
        elif nums[mid] > value:
            right = mid - 1
        else:
            return mid
    return 0
  

nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 6)
print(index) # 2


def linear_search(nums, value):
    for i in range(len(nums)):
        print(f"i:{i} nums[{i}] --> {nums[i]}")
        if value == nums[i]:
            return i
    return 0


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 6)
print(index) # 2


'''
Version 3 - Bubble Sort (optional)

Bubble sort is one of the simplest and least efficient sorting algorithms. 
We repeatedly loop over the list, comparing each number to the one next 
to it, and swapping them if needed.
'''
# def bubble_sort(slist):
#     n = len(slist)
#     need_swap = True
#     while need_swap:
#         for i in range(n - 1):
#             print(f"i:{i} slist[{i}] --> {slist[i]}")
#             # if this pair is out of order
#             if slist[i - 1] > slist[i]:
#                 # swap them and remember something changed 
#                 tmp = slist[i - 1] 
#                 slist[i - 1] = slist[i]
#                 slist[i] = tmp
#                 need_swap = False
    

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# bubble_sort(nums)
# print(nums)


def bubble_sort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
        # Last i elements are already in place 
        print(f"Bubble Sort Insertion sort: i:{i}")
        for j in range(0, n-i-1): 
            print(f"j:{j} slist[{j}] --> {arr[j]}")
            # traverse the array from 0 to n-i-1 Swap if the element found is greater than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
bubble_sort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  


'''
# Version 4 - Insertion Sort (optional)
# Implement insertion sort, which like bubble sort is also O(n^2), 
# but is efficient at placing new values into an already-sorted list.
# Python program for implementation of Insertion Sort 
'''
  
# Function to do insertion sort 
def insertion_sort(slist): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(slist)): 
        key = slist[i] 
        # Move elements of slist[0..i-1], that are greater than key, to one position ahead of their current position 
        j = i-1
        print(f"Insertion sort: i:{i} j:{j}")
        while j >=0 and key < slist[j]: 
                print(f"j:{j} slist[{j}] --> {slist[j]}")
                slist[j+1] = slist[j] 
                j -= 1
        slist[j+1] = key 
  
  
# Driver code to test above 
# slist = [12, 11, 13, 5, 6] 
# insertion_sort(slist) 
# print ("Sorted array is:") 
# for i in range(len(slist)): 
#     print ("%d" %slist[i]) 


'''
# Quicksort is one of the most efficient sorting algorithms. It works by swapping elements 
# on either side of a pivot value. Python program for implementation of Quicksort Sort 
# This function takes last element as pivot, places the pivot element at its correct position 
# in sorted array, and places all smaller (smaller than pivot)to left of pivot and all 
# greater elements to right of pivot
''' 
 
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    print(f"Quick sort: i:{i} j:{j}")
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


 
 
def reverse_number(number: int):
    reversed = 0   
    while number != 0:
        digit = number % 10
        reversed = reversed * 10 + digit
        number //= 10
    return  reversed


num = 10025
print(f"Input - {num} Output: {reverse_number(num)}")


class Factorial():
 
  def factorial_with_loop(self, n: int):
    if n < 0:
      print("Negative nos can't have factorial")
      return 0
    fact = 1
    for i in range(2,n):
      fact = fact * i
    return fact
 
  def factorial_with_recursion(self, n: int):
    if n < 0:
      print("Negative nos can't have factorial")
      return 0
    if n <= 2:
      return n
    return n * self.factorial_with_recursion(n - 1)


fact = Factorial()
print(f"Factorial of 10 using loop is:{fact.factorial_with_loop(10)}")
print(f"Factorial of 10 using recursion is:{fact.factorial_with_recursion(10)}")
print(f"Factorial of negative number -100 is:{fact.factorial_with_loop(-100)}")
 
# lambda
x = lambda a, b : a * b
print(x(5, 6))

# map + lambda
letters = list(map(lambda x: x, 'human'))
print(letters)

# list comprehension
h_letters = [ letter for letter in 'human' ]
print( h_letters)