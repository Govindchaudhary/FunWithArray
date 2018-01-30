nums = [1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]

def arraySum(nums,sum):
    list = []
    for i in xrange(len(nums)):
        for j in xrange(i+1,len(nums)) :
            if (nums[i] + nums[j] ==sum) and ( (nums[j],nums[i])  not in list):
                list.append((nums[i],nums[j]))
                break
    return list


print arraySum(nums,10)
               