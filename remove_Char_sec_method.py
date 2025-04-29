def add_charcters (s,stars) :      #How to insert characters in a string at a certain position?
    k=0
    for i in range(len(stars)):
        s = s[:stars[i]+k] + '*' + s [stars[i]+k:]
        k +=1

    return s
s="hello"
stars=[0,2,4]
print(add_charcters(s,stars))

                            