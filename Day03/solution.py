from time import sleep
import sys

def missing_element(arr):
    duplicate = None
    for i, element in enumerate(arr):
        if element < 0:
            arr[i] = duplicate
        elif not duplicate:
            duplicate = element
    for i, element in enumerate(arr):
        if element != i+1:
            arr[i], j = None, element
            while j is not None and arr[j-1] != j:
                arr[j-1], j = j, arr[j-1]
    for i, element in enumerate(arr):
        if not element:
            return i+1
    return len(arr)
