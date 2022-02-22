import random
import time
#import numpy as np


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


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

i = 0
f = open("teste.in ")
nrteste = f.readline()
for teste in f:
    if i == int(nrteste):
        break

    aux = teste.split()

    arr =  [random.randrange(1, int(aux[1])) for i in range(int(aux[0]))]
    #arr = list(np.random.randint(low = 0,high=int(aux[1]),size=int(aux[0])))

    i +=1
    print("Sir initial ", end="\n")
    printList(arr)
    start = time.time()
    mergeSort(arr)
    stop = time.time()
    print("Sir sortat",end="\n")
    printList(arr)

    print("Timp: ", stop - start, "secunde", end="\n\n")

