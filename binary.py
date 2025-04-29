def isBinary(s): #Check for Binary String
    for i in range(len(s)):
      
        if s[i] != '0' and s[i] != '1':
            return False
    return True

s = "01010101010"
