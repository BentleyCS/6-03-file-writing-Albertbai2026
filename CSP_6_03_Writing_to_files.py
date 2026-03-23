import random
from typing import List, Tuple

def bubbleSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using bubble sort and count swaps & comparisons."""
    swaps = comparisons = 0
    items = items.copy()
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return items, swaps, comparisons

def insertionSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using insertion sort and count shifts & comparisons."""
    shifts = comparisons = 0
    items = items.copy()
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                shifts += 1
                j -= 1
            else:
                break
        items[j + 1] = key
    return items, shifts, comparisons

def selectionSort(items: List[int]) -> Tuple[List[int], int, int]:
    """Sort a list using selection sort and count swaps & comparisons."""
    swaps = comparisons = 0
    items = items.copy()
    n = len(items)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            swaps += 1
    return items, swaps, comparisons

def printResults(name: str, result: Tuple[List[int], int, int]):
    sorted_list, moves, comparisons = result
    print(f"{name}:")
    print(f"  Sorted list  = {sorted_list}")
    print(f"  Moves        = {moves}")
    print(f"  Comparisons  = {comparisons}\n")

if __name__ == "__main__":
    print("=== Worst Case (Reverse Sorted List) ===")
    y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    printResults("Bubble Sort",    bubbleSort(y))
    printResults("Insertion Sort", insertionSort(y))
    printResults("Selection Sort", selectionSort(y))

    print("=== Random List ===")
    x = list(range(50))
    random.shuffle(x)
    printResults("Bubble Sort",    bubbleSort(x))
    printResults("Insertion Sort", insertionSort(x))
    printResults("Selection Sort", selectionSort(x))
