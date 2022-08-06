

def countSwaps(array):
    swap=0
    n=len(array)
    for j in range(n-1):
        for i in range(n-1):
            if (array[i]>array[i+1]):
                array[i],array[i+1]=array[i+1], array[i]
                swap+=1
    print("Array is sorted in",swap, "swaps.")
    print("First Element:",array[0])
    print("Last Element:",array[-1])