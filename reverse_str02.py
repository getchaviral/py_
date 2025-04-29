def reverse(s):
    n =len(s)
    res =""
    for i in range(-1,-n-1,-1):
        res += s[i]
    return res

print(reverse("str"))



        
