def countingSort(arr):
    # Write your code here
    output = [0] * 100
    for item in arr:
        output[item] += 1
    return output
