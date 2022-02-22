import random
import time
import numpy as np
import sys

#singura sansa la python sort e sa dai nr de numere minim 1000
#noteaza faptul ca quicksort la 1000 nu merge pe 1000 de numere, dar la recursionlimit 1500 merge, iar pe 100 de numere merge oricum, dupa nu mai merge quicksort.


def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1


def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

def heapify(arr, n, i):
  largest = i  # Initialize largest as root
  l = 2 * i + 1  # left = 2*i + 1
  r = 2 * i + 2  # right = 2*i + 2

  # See if left child of root exists and is
  # greater than root
  if l < n and arr[largest] < arr[l]:
    largest = l

  # See if right child of root exists and is
  # greater than root
  if r < n and arr[largest] < arr[r]:
    largest = r

  # Change root, if needed
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # swap

    # Heapify the root.
    heapify(arr, n, largest)

def heapSort(arr):
  n = len(arr)

  # Build a maxheap.
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # One by one extract elements
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]  # swap
    heapify(arr, i, 0)

def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def shellSort(arr):
    gap = len(arr) // 2  # initialize the gap

    while gap > 0:
        i = 0
        j = gap

        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1

            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1

        gap //= 2

def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def insertionSort(arr):
  # Traverse through 1 to len(arr)
  for i in range(1, len(arr)):

    key = arr[i]

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10


def bubbleSort(arr):
  n = len(arr)

  # Traverse through all array elements
  for i in range(n):

    # Last i elements are already in place
    for j in range(0, n - i - 1):

      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()





c = 0
f = open("teste.in")
nrteste = f.readline()
for teste in f:
    if c == int(nrteste):
        break

    aux = teste.split()

    arr =  [random.randrange(1, int(aux[1])) for i in range(int(aux[0]))]
    aux1 = arr
    #arr = list(np.random.randint(low = 0,high=int(aux[1]),size=int(aux[0])))

    c +=1
    print(f"N={int(aux[0])} Max = {int(aux[1])} \n ")
    print("Sir initial ", end="\n")
    printList(arr)

    #MergeSort
    start = time.time()
    mergeSort(arr)
    stop = time.time()
    arr = aux1
    print("Sir sortat",end="\n")
    printList(arr)
    print()
    print("Timp Merge sort: ", stop-start, "secunde", end="\n\n")

    # Built-in Sorting Algorithm
    start = time.time()
    arr = sorted(arr)
    stop = time.time()
    arr = aux1
    print("Timp Python Sort:", stop - start, "secunde", end="\n\n")

    #RadixSort
    start = time.time()
    radixSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Radix Sort: ", stop-start , "secunde", end="\n\n")

    # QuickSort
    #if int(aux[0]) < 1000:
     #  start = time.time()
      # quickSort(arr, 0, len(arr) - 1)
       #stop = time.time()
      # arr = aux1
       #print("Timp Quick Sort: ", stop - start, "secunde", end="\n\n")
   # else:
    #  print("Quicksort nu poate")
    #  print()

    # HeapSort
    start = time.time()
    heapSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Heap Sort : ", stop - start, "secunde", end="\n\n")

    # Insertion Sort
    start = time.time()
    insertionSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Insertion : ", stop - start, "secunde", end="\n\n")

    # Bubble Sort
    start = time.time()
    bubbleSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Bubble Sort:", stop - start, "secunde", end="\n\n")

    # ShellSort
    if int(aux[0]) < 10001:
      start = time.time()
      shellSort(arr)
      stop = time.time()
      arr = aux1
      print("Timp Shell Sort: ", stop - start, "secunde", end="\n\n")
    else:
        print("Dureaza prea mult Shell-Sort")


