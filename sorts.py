import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1


        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i


            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


def hibbard_sequence(n):

    k = 1
    gaps = []
    while (gap := 2 ** k - 1) <= n:
        gaps.append(gap)
        k += 1
    return gaps[::-1]


def shell_hibbard_sort(arr):
    n = len(arr)
    gaps = hibbard_sequence(n)

    for gap in gaps:

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp


def pratt_sequence(n):

    gaps = []
    p, q = 0, 0

    while True:
        gap = (2 ** p) * (3 ** q)
        if gap > n:
            if q == 0:
                p += 1
            else:
                q -= 1
                continue
        else:
            gaps.append(gap)
            if q == 0:
                p += 1
            else:
                q += 1
        if gap > n and p > 0 and q == 0:
            break

    return sorted(gaps)


def shell_pratt_sort(arr):

    n = len(arr)
    gaps = pratt_sequence(n)

    for gap in gaps:

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2


    if left < n and arr[left] > arr[largest]:
        largest = left


    if right < n and arr[right] > arr[largest]:
        largest = right


    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)






