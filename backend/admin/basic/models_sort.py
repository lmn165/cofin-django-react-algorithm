from dataclasses import dataclass


class Sorting(object):

    random_arr :[]

    @property
    def random_arr(self) -> []: return self._random_arr

    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr)
        # print('\n')
        for i in range(n -1):
            for j in range(n -i -1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr)
            # print("\n")
        return arr

    @staticmethod
    def merge_sort(random_arr:[] ):
        if len(random_arr) < 2:
            return random_arr
        arr = random_arr
        mid = len(arr) // 2
        left = Sorting.merge_sort(arr[:mid])
        right = Sorting.merge_sort(arr[mid:])
        merged_arr = []
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged_arr.append(left[l])
                l += 1
            else:
                merged_arr.append(right[r])
                r += 1
        merged_arr += left[l:]
        merged_arr += right[r:]
        return merged_arr

    @staticmethod
    def quick_sort(random_arr:[]):
        arr = random_arr
        if len(arr) < 2:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], []
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)