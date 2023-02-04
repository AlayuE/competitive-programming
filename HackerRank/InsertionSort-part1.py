def insertionSort1(n, arr):
    # Write your code here
    last_element = arr[-1]
    
    for i in range(n-1,-1,-1):
        if arr[i-1] > last_element and i != 0:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = last_element
            print(*arr)
            break 
