def finder(arr1,arr2):
    sum1=0
    sum2=0
    for i in arr1:
        sum1+=i
    for j in arr2:
        sum2+=j
    return sum1-sum2 

print finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])