def largestSum1(arr):
    sum1=0
    
    sumList = []
    for i in arr:
       sum1+=i
       if sum1 < 0:
          sum1=0
       if  sum1>0 and sum1 not in sumList :
          sumList.append(sum1)
          
    return sumList
print 'for my case'       
print largestSum1([1,2,-1,3,4,10,10,-10,-1])


print 'solution'
def largestSum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        print current_sum
        max_sum = max(current_sum,max_sum)
    return max_sum

largestSum([1,2,-1,3,4,10,10,-10,-1])
       
       