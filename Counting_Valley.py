def countingValleys(steps, path):
    sum = 0
    count = 0
    result = [1 if i == "U" else -1 for i in path]
    for i, ele in enumerate(result):
        sum += ele
        if sum == 0 and result[i] == 1:
            count += 1
    return count