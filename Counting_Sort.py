
def countingSort(array):
    tally = [0] * 100
    
    for i in array:
        tally[i] += 1
    return tally

