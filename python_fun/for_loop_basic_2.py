def biggieSize(arr):
  for i in range(0,len(arr),1):
    if arr[i] > 0:
      arr[i] = "big"
  return arr
print(biggieSize([-5,2,4,-1]))

def countPos(arr):
  count = 0
  for i in range(0,len(arr),1):
    if arr[i] > 0:
      count += 1
  arr[len(arr)-1] = count
  return arr
print(countPos([-5,2,4,-1]))

def sumTotal(arr):
  total = 0
  for i in range(0,len(arr),1):
    total += arr[i]
  return total
print(sum([1,2,3,4,5]))

def Average(arr):
  total = 0
  for i in range(0,len(arr),1):
    total += arr[i]
  avg = total / len(arr)
  return avg
print(Average([1,2,3,4,5]))

def length(arr):
  return len(arr)
print(length([1,2,3,4,5,6]))

def returnMin(arr):
  min = arr[0]
  if len(arr) = 0:
    return false
  for i in range(0,len(arr),1):
    if min < arr[i]:
      min = arr[i]
  return min
print(returnMin([1,-3,6,0,7]))

def returnMax(arr):
  max = arr[0]
  if len(arr) = 0:
    return false
  for i in range(0,len(arr),1):
    if max > arr[i]:
      max = arr[i]
  return max
print(returnMin([1,-3,6,0,7]))

def ultimateAnalyze(arr):
  total = 0
  minimum = arr[0]
  maximum = arr[0]
  length = len(arr)
  for i in range(0,len(arr),1):
    total += arr[i]
    if arr[i] < minimum:
      minimum = arr[i]
      print(minimum)
    if arr[i] > maximum:
      maximum = arr[i]
  average = total / length
  analyzed = {"Sum":total,"Average":average,"Min":minimum,"Max":maximum,"Length":length}
  return analyzed
print(ultimateAnalyze([1,2,3,4,5]))

def reverse(arr):
  temp = 0
  count = 0
  while len(arr)/2 > count:
    temp = arr[count]
    arr[count] = arr[len(arr) - count - 1]
    arr[len(arr) - count - 1] = temp
    count += 1
  return arr
print(reverse([1,2,3,4,5,6]))