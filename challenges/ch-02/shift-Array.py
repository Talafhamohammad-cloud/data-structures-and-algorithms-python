value1=10
array1 = [15, 5, 22, 17, 45]
value2=2
array2=[22,61,85,88,99,65]
value3=5
array3=[]
############################################################################
def insertShiftArray(array, V):
  if not(type(array) == type([])):
    return 'error'
  newArr = []
  if len(array) % 2 == 0:
    S = int(len(array)/2)
  else:
    S = int(len(array)/2)+1
  newArr = array[0:S]+[V]
  newArr = newArr+array[S:len(array)]

  return newArr
##########################################################################

print(insertShiftArray(array2, value2))
print(insertShiftArray(array1, value1))
print(insertShiftArray(array3, value3))
