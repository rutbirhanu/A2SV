class Solution:
    # def select(self, arr, i):
    # code here

    def selectionSort(self, array, n):
        # code here
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if array[j] < array[min]:
                    min = j
            if (min != i):
                array[min], array[i] = array[i], array[min]

        return array



