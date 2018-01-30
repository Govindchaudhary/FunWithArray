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

def anagram(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    count = 0
    if len(str1)!=len(str2) :
       print 'No'
    for ch in removeDuplicates(str1):
       if countChar(str1,ch)==countChar(str2,ch):
          count +=1
       else:
          break
    if count==len(removeDuplicates(str1)):
       print 'yes'


anagram('hi man','hi      ma     N')       



         