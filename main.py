import random
import time
import copy


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

        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


def shellSort(arr, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2


def insertionSort(arr):
    for pas in range(1, len(arr)):
        cheie = arr[pas]
        j = pas - 1
        while j >= 0 and cheie < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cheie


def countingSort(arr, loc):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = arr[i] // loc
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // loc
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radixSort(arr):

    elem_max = max(arr)

    loc = 1
    while elem_max // loc > 0:
        countingSort(arr, loc)
        loc *= 10


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux


def counting_sort(arr, val_maxima):

    counts = [0] * (val_maxima + 1)
    for item in arr:
        counts[item] += 1

    num_items_bef = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_bef
        num_items_bef += count

    sorted_list = [None] * len(arr)

    for item in arr:
        sorted_list[counts[item]] = item
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
    start = time.time()
    mergeSort(arr)
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Merge sort: ", stop - start, "secunde", end="\n\n")

    # Radix Sort
    print(arr)
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
    if int(aux[0]) < 100001:
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
    if int(aux[0]) < 100001:
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

    # Couting Sort
    arr = auxCounting
    start = time.time()
    arr = counting_sort(arr, max(arr))
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Counting sort: ", stop - start, "secunde", end="\n\n")

    # Python sort
    arr = auxPython
    start = time.time()
    stop = time.time()
    if arr == sorted(arr):
        print(f"Correct = True")
    else:
        print(f"Correct = False")
    print("Timp Python Sort: ", stop - start, "secunde", end="\n\n")
