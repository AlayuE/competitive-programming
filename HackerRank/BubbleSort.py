def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)):
        for j in range(len(a)- i -1):
              if (a[j] > a[j + 1]):
                count +=1
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp   
    print( f'Array is sorted in {count} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}')     
