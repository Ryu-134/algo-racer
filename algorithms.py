import random
from typing import List

class SortingAlgorithms:
    @staticmethod
    def _merge(arr, left, mid, right, state):
        left_copy = arr[left:mid + 1]
        right_copy = arr[mid + 1:right + 1]
        state.accesses += len(left_copy) + len(right_copy)
        i = j = 0
        k = left
        while i < len(left_copy) and j < len(right_copy):
            state.highlighted = [k]
            state.comparisons += 1
            yield True
            if left_copy[i] <= right_copy[j]:
                arr[k] = left_copy[i]
                i += 1
            else:
                arr[k] = right_copy[j]
                j += 1
            state.accesses += 1
            k += 1
        while i < len(left_copy):
            state.highlighted = [k]
            arr[k] = left_copy[i]
            state.accesses += 1
            i += 1
            k += 1
            yield True
        while j < len(right_copy):
            state.highlighted = [k]
            arr[k] = right_copy[j]
            state.accesses += 1
            j += 1
            k += 1
            yield True

    @staticmethod
    def _sift_down(arr, n, i, state):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        state.highlighted = [i, left if left < n else i]
        yield True
        if left < n:
            state.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            state.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            state.accesses += 2
            yield True
            yield from SortingAlgorithms._sift_down(arr, n, largest, state)

    @staticmethod
    def _counting_sort_digit(arr, exp, state):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            idx = (arr[i] // exp) % 10
            count[idx] += 1
            state.highlighted = [i]
            state.accesses += 1
            yield True
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            state.highlighted = [i]
            idx = (arr[i] // exp) % 10
            output[count[idx] - 1] = arr[i]
            count[idx] -= 1
            state.accesses += 2 
            yield True
        for i in range(n):
            arr[i] = output[i]
            state.highlighted = [i]
            state.accesses += 1 
            yield True

    @staticmethod
    def _stooge_recursive(arr, l, h, state):
        if l >= h: return
        state.comparisons += 1
        state.highlighted = [l, h]
        yield True
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
            state.accesses += 2
            yield True
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            yield from SortingAlgorithms._stooge_recursive(arr, l, h - t, state)
            yield from SortingAlgorithms._stooge_recursive(arr, l + t, h, state)
            yield from SortingAlgorithms._stooge_recursive(arr, l, h - t, state)

    @staticmethod
    def _quick_sort_recursive(arr, low, high, state):
        if low < high:
            pivot_index = yield from SortingAlgorithms._partition(arr, low, high, state)
            yield from SortingAlgorithms._quick_sort_recursive(arr, low, pivot_index - 1, state)
            yield from SortingAlgorithms._quick_sort_recursive(arr, pivot_index + 1, high, state)

    @staticmethod
    def _partition(arr, low, high, state):
        pivot = arr[high]
        state.accesses += 1
        state.pivot_index = high
        i = low - 1
        for j in range(low, high):
            state.highlighted = [j, high]
            state.comparisons += 1
            yield True
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                state.accesses += 2
                yield True
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        state.accesses += 2
        state.pivot_index = -1
        yield True
        return i + 1

    @staticmethod
    def _merge_sort_recursive(arr, left, right, state):
        if left < right:
            mid = (left + right) // 2
            yield from SortingAlgorithms._merge_sort_recursive(arr, left, mid, state)
            yield from SortingAlgorithms._merge_sort_recursive(arr, mid + 1, right, state)
            yield from SortingAlgorithms._merge(arr, left, mid, right, state)


    @staticmethod
    def bubble_sort(arr, state):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                state.highlighted = [j, j+1]
                state.comparisons += 1
                yield True 
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    state.accesses += 2
                    swapped = True
                    yield True
            if not swapped: break
        state.highlighted = []

    @staticmethod
    def cocktail_shaker_sort(arr, state):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                state.highlighted = [i, i+1]
                state.comparisons += 1
                yield True
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    state.accesses += 2
                    swapped = True
                    yield True
            if not swapped: break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                state.highlighted = [i, i+1]
                state.comparisons += 1
                yield True
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    state.accesses += 2
                    swapped = True
                    yield True
            start += 1
        state.highlighted = []

    @staticmethod
    def comb_sort(arr, state):
        n = len(arr)
        gap = n
        shrink = 1.3
        sorted_ = False
        while not sorted_:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_ = True
            i = 0
            while i + gap < n:
                state.highlighted = [i, i+gap]
                state.comparisons += 1
                yield True
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    state.accesses += 2
                    sorted_ = False
                    yield True
                i += 1
        state.highlighted = []

    @staticmethod
    def odd_even_sort(arr, state):
        n = len(arr)
        sorted_ = False
        while not sorted_:
            sorted_ = True
            for i in range(1, n-1, 2):
                state.highlighted = [i, i+1]
                state.comparisons += 1
                yield True
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    state.accesses += 2
                    sorted_ = False
                    yield True
            for i in range(0, n-1, 2):
                state.highlighted = [i, i+1]
                state.comparisons += 1
                yield True
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    state.accesses += 2
                    sorted_ = False
                    yield True
        state.highlighted = []

    @staticmethod
    def insertion_sort(arr, state):
        for i in range(1, len(arr)):
            key = arr[i]
            state.accesses += 1
            j = i - 1
            state.highlighted = [i]
            yield True
            while j >= 0:
                state.comparisons += 1
                if key < arr[j]:
                    state.highlighted = [j, j+1]
                    arr[j + 1] = arr[j]
                    state.accesses += 1
                    j -= 1
                    yield True
                else:
                    break
            arr[j + 1] = key
            state.accesses += 1
            yield True
        state.highlighted = []

    @staticmethod
    def gnome_sort(arr, state):
        index = 0
        n = len(arr)
        while index < n:
            if index == 0: index += 1
            state.highlighted = [index, index-1]
            state.comparisons += 1
            yield True
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                state.accesses += 2
                yield True
                index -= 1
        state.highlighted = []

    @staticmethod
    def shell_sort(arr, state):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                state.accesses += 1
                j = i
                state.highlighted = [i]
                yield True
                while j >= gap:
                    state.comparisons += 1
                    if arr[j - gap] > temp:
                        state.highlighted = [j, j - gap]
                        arr[j] = arr[j - gap]
                        state.accesses += 1
                        j -= gap
                        yield True
                    else: break
                arr[j] = temp
                state.accesses += 1
                yield True
            gap //= 2
        state.highlighted = []

    @staticmethod
    def selection_sort(arr, state):
        n = len(arr)
        for i in range(n):
            min_idx = i
            state.highlighted = [i]
            yield True
            for j in range(i + 1, n):
                state.highlighted = [i, j]
                state.comparisons += 1
                yield True
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                state.accesses += 2
                yield True
        state.highlighted = []

    @staticmethod
    def quick_sort(arr, state):
        yield from SortingAlgorithms._quick_sort_recursive(arr, 0, len(arr) - 1, state)

    @staticmethod
    def merge_sort(arr, state):
        yield from SortingAlgorithms._merge_sort_recursive(arr, 0, len(arr) - 1, state)

    @staticmethod
    def heap_sort(arr, state):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            yield from SortingAlgorithms._sift_down(arr, n, i, state)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            state.accesses += 2
            state.highlighted = [0, i]
            yield True
            yield from SortingAlgorithms._sift_down(arr, i, 0, state)

    @staticmethod
    def tim_sort(arr, state):
        n = len(arr)
        min_run = 32
        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            for i in range(start + 1, end + 1):
                key = arr[i]
                state.accesses += 1
                j = i - 1
                state.highlighted = [i]
                yield True
                while j >= start:
                    state.comparisons += 1
                    if arr[j] > key:
                        state.highlighted = [j, j+1]
                        arr[j + 1] = arr[j]
                        state.accesses += 1
                        j -= 1
                        yield True
                    else: break
                arr[j + 1] = key
                state.accesses += 1
                yield True
        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), n - 1)
                if mid < right:
                    yield from SortingAlgorithms._merge(arr, left, mid, right, state)
            size *= 2
        state.highlighted = []

    @staticmethod
    def stooge_sort(arr, state):
        yield from SortingAlgorithms._stooge_recursive(arr, 0, len(arr) - 1, state)
        state.highlighted = []

    @staticmethod
    def counting_sort(arr, state):
        if not arr: return
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for i, num in enumerate(arr):
            state.highlighted = [i]
            state.accesses += 1 
            count[num] += 1
            state.accesses += 1 
            yield True
        arr_idx = 0
        for val, freq in enumerate(count):
            for _ in range(freq):
                state.highlighted = [arr_idx]
                arr[arr_idx] = val
                state.accesses += 1 
                yield True
                arr_idx += 1
        state.highlighted = []

    @staticmethod
    def bucket_sort(arr, state):
        if not arr: return
        n = len(arr)
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        buckets = [[] for _ in range(n)]
        for i, x in enumerate(arr):
            state.highlighted = [i]
            idx = int((x - min_val) * n / (range_val + 1)) 
            buckets[idx].append(x)
            state.accesses += 2 
            yield True
        for b in buckets: b.sort()
        k = 0
        for b in buckets:
            for x in b:
                state.highlighted = [k]
                arr[k] = x
                state.accesses += 1
                yield True
                k += 1
        state.highlighted = []

    @staticmethod
    def radix_sort(arr, state):
        if not arr: return
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            yield from SortingAlgorithms._counting_sort_digit(arr, exp, state)
            exp *= 10