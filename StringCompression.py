def countChar(str,char):
    count=0
    for ch in str:
       if ch==char:
         count +=1
    return count

def removeDuplicates(string):
    str =""
    for ch in string:
       if ch  not in str:
           str+=ch
    return str


def stringCompression(string):
   newString = removeDuplicates(string)
   for char in newString:
     newString =  newString.replace(char, char + str(countChar(string,char)))
   
   print newString




stringCompression('sdfxgcvhmnjpoiioppoiuytrdfghjkll')
      