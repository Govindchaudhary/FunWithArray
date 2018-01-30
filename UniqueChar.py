def unique(string):
   string2 = ""
   for char in string:
      if char not in string2:
         string2+=char
   if string == string2:
     return True
   else:
       return False

print unique('poiuytrewq')