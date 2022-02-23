import random
import time
import numpy as np
import sys

# singura sansa la python sort e sa dai nr de numere minim 1000
# noteaza faptul ca quicksort la 1000 nu merge pe 1000 de numere,
# dar la recursionlimit 1500 merge, iar pe 100 de numere merge oricum, dupa nu mai merge quicksort.
# Daca dureaza prea mult, facem error handling si afisam
# spre exemplu ca dureaza prea mult, iar la quicksort incercam sa l facem iterativ


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
    r = 2 * i + 2  #

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

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
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1

            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1

        gap //= 2


def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def countingSortForRadix(inputArray, placeValue):
    # We can assume that the number of digits used to represent
    # all numbers on the placeValue position is not grater than 10
    countArray = [0] * 10
    inputSize = len(inputArray)

    # placeElement is the value of the current place value
    # of the current element, e.g. if the current element is
    # 123, and the place value is 10, the placeElement is
    # equal to 2
    for i in range(inputSize):
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    # Reconstructing the output array
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def radixSort(inputArray):
    # Step 1 -> Find the maximum element in the input array
    maxEl = max(inputArray)

    # Step 2 -> Find the number of digits in the `max` element
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1

    # Step 3 -> Initialize the place value to the least significant place
    placeVal = 1

    # Step 4
    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10
        D -= 1

    return outputArray


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


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

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

    arr = [random.randrange(1, int(aux[1])) for i in range(int(aux[0]))]
    aux1 = arr
    # arr = list(np.random.randint(low = 0,high=int(aux[1]),size=int(aux[0])))

    c += 1
    print(f"N={int(aux[0])} Max = {int(aux[1])} \n ")
    print("Sir initial ", end="\n")
    # printList(arr)

    # MergeSort
    start = time.time()
    mergeSort(arr)
    stop = time.time()
    arr = aux1
    print("Sir sortat", end="\n")
    printList(arr)
    print()
    print("Timp Merge sort: ", stop - start, "secunde", end="\n\n")

    # Built-in Sorting Algorithm
    start = time.time()
    arr = sorted(arr)
    stop = time.time()
    arr = aux1
    print("Timp Python Sort:", stop - start, "secunde", end="\n\n")

    # RadixSort
    start = time.time()
    arr = radixSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Radix Sort: ", stop - start, "secunde", end="\n\n")

    # HeapSort
    start = time.time()
    heapSort(arr)
    stop = time.time()
    arr = aux1
    print("Timp Heap Sort : ", stop - start, "secunde", end="\n\n")

    # Insertion Sort
    arr = sorted(arr, reverse=True)
    # Daca faci reverse=true nu mai merge atat de bine insertion sort-ul.
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

    # Quick Sort
    # if int(aux[0]) < 10000:
    #    start = time.time()
    #   quick_sort(0, len(arr) - 1, arr)
    #  stop = time.time()
    # print("Timp Quick Sort:", stop - start, "secunde", end="\n\n")

    # ShellSort
    if int(aux[0]) < 10000:
        start = time.time()
        shellSort(arr)
        stop = time.time()
        arr = aux1
        print("Timp Shell Sort: ", stop - start, "secunde", end="\n\n")
    else:
        print("Dureaza prea mult Shell-Sort")
