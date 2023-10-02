def bubbleSort(arr):
    for i in range(len(arr)): 
        swapped = False
        for j in range(0, len(arr)-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if not swapped: 
            break
    return arr
lst = list (map(int, input().split()))
ans = bubbleSort(lst) 
print("Bubble Sort:",ans)