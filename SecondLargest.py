
arr = [int(num) for num in input().strip().split(' ')]

first = second = -2147483648

if len(arr) < 2 :
     print('no 2nd highest element exist')
else:

  for i in range(len(arr)):
     if arr[i]>first:
        second = first
        first = arr[i]
     elif arr[i]>second and arr[i]<first:
        second = arr[i]

  if second==-2147483648:
    print('no 2nd highest element exist')
  else:
   print('second highest element is:' + ' ' + str(second))