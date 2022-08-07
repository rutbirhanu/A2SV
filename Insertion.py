
def insertionSort1(n, array):
     for i in range(n-1,1,-1):
        current=array[i]
        pos=i

        while current <array[pos-1] and pos>0:
            array[pos]=array[pos-1]
            print(*array)
            pos-=1
        array[pos]=current
     print(*array)