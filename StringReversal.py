def reverse(string):
   list1 = string.split()
   for i in xrange(len(list1)/2):
       list1[i], list1[len(list1)-i-1] = list1[len(list1)-i-1], list1[i]  #swapping
   print ' '.join(list1)


#s1, s2 = s2, s1  for swapping s1 and s2
reverse("  this is test")




      