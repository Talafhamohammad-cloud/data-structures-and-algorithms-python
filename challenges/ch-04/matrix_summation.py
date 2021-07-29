matrix =[[1,-2,3,-1],[4,-1,-3],[1,-3,1]]

def matsum(matrix):
  newmat=[]
  for i in matrix:
    sum =0
    for j in i:
      sum=sum+j

    newmat=newmat+[sum]
  return newmat   
print(matsum(matrix))
