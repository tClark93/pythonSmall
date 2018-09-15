def countDown(num):
  for i in range(num,-1,-1):
    print(i)
countDown(5)

def printReturn(arr):
  print (arr[0])
  return arr[1]
printReturn([3,4])

def firstPlusLength(arr):
  return arr[0]+len(arr)
print(firstPlusLength([3,4,5,6]))

arrnew = []
def greaterThanSecond(arr):
  for i in range(0,len(arr)-1,1):
    if arr[i] > arr[1]:
      arrnew.append(arr[i])
  return arrnew
print(greaterThanSecond([8,4,5,6,2]))

arr = []
def lengthValue(num1,num2):
  if num1 == num2:
    print("jynx!")
  for i in range(0,num1,1):
    arr.append(num2)
  return arr
print(lengthValue(5,5))