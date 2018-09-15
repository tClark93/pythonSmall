def selectionSort(arr):
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      min=arr[j]
      if min > arr[j]:
        min = arr[j]
        print(min)
      if arr[i] > min:
        print(arr[i], min)
        arr[j], arr[i] = arr[i], arr[j]
  return arr

print(selectionSort([4,8,2,1,5,7]))
