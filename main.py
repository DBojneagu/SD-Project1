import random
import time
import numpy as np
import sys
import copy


def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

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


def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


def partition(start, end, array):

    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if start < end:

        p = partition(start, end, array)

        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


def bubbleSort(array):
    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def counting_sort(the_list, max_value):

    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # etc.
    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1

    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(the_list)

    # Run through the input list
    for item in the_list:

        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list

c = 0
f = open("teste.in")
nrteste = f.readline()
for teste in f:
    if c == int(nrteste):
        break

    aux = teste.split()

    prearr = [random.randrange(1, int(aux[1])) for i in range(int(aux[0]))]
    arr = prearr
    auxMerge = copy.deepcopy(prearr)
    auxRadix = copy.deepcopy(prearr)
    auxHeap = copy.deepcopy(prearr)
    auxShell = copy.deepcopy(prearr)
    auxBubble = copy.deepcopy(prearr)
    auxInsertion = copy.deepcopy(prearr)
    auxCounting = copy.deepcopy(prearr)
    auxPython = copy.deepcopy(prearr)

    c += 1

    print(f"Sir {c} \n N={int(aux[0])} Max = {int(aux[1])} \n ")

    # MergeSort
    arr = auxMerge
    start = time.time()
    mergeSort(arr)
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Merge sort: ", stop - start, "secunde", end="\n\n")

    # Radix Sort
    arr = auxRadix
    start = time.time()
    radixSort(arr)
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(arr)
        print(f"Correct = False")
    print("Timp Radix sort: ", stop - start, "secunde", end="\n\n")

    # Heap Sort
    arr = auxHeap
    start = time.time()
    heapSort(arr)
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Heap sort: ", stop - start, "secunde", end="\n\n")

    # Insertion Sort
    if int(aux[0]) < 10001:
        arr = auxInsertion
        start = time.time()
        insertionSort(arr)
        stop = time.time()
        if arr == sorted(arr):
            print(f"Correct = True")
        else:
            print(f"Correct = False")
        print("Timp Insertion sort: ", stop - start, "secunde", end="\n\n")
    else:
        print("Prea mult pentru insertion")
        print()
    # Bubble Sort
    if int(aux[0]) < 10001:
        arr = auxBubble
        start = time.time()
        bubbleSort(arr)
        stop = time.time()
        if arr == sorted(arr):
            print(f"Correct = True")
        else:
            print(f"Correct = False")

        print("Timp Bubble sort: ", stop - start, "secunde", end="\n\n")
    else:
        print("Prea mult pentru Bubble Sort")
        print()
    # ShellSort
    arr = auxShell
    start = time.time()
    shellSort(arr, len(arr))
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Shell sort: ", stop - start, "secunde", end="\n\n")

    #Couting Sort
    arr = auxCounting
    start = time.time()
    arr =  counting_sort(arr,max(arr))
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Counting sort: ", stop - start, "secunde", end="\n\n")

    #Python sort
    arr = auxPython
    start = time.time()
    arr = sorted(arr)
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Python Sort: ", stop - start, "secunde", end="\n\n")

