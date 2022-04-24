def countingSort(arr):
    maxElement = max(arr)
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength
    
    for i in arr: 
        countArray[i] += 1
        
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    array = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        x = arr[i]
        countArray[x] -= 1
        newPosition = countArray[x]
        array[newPosition] = x
        i -= 1

    return array

arr = [2,2,0,6,1,9,9,7]
print("Input array = ", arr)

sortedArray = countingSort(arr)
print("Counting sort result = ", sortedArray)