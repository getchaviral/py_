#Remove a Character from a Given Position
def removechar (s,pos):
    if (pos<0 or pos>len(s)):
        return s
    return s[:pos] + s[pos+1:]

print (removechar("aba",2))

