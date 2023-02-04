class Solution: 
    def select(self, arr, i):
        # code here 
        x = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[x]:
                x = j
        return x
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1,-1,-1):
            j = self.select(arr,i)
            arr[i],arr[j]= arr[j],arr[i]
