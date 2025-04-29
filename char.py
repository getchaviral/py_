def insertchar (s,c,pos): #Insert a character in String at a Given Position (also can be done by built in methods)
    res = ""
    for i in range(len(s)):
         
         if i==pos:
              res +=c
              

         res += s[i]
    
    return res

print (insertchar("na","d",1))


