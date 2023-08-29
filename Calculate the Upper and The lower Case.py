s=(input("enter a string:"))
def upperlowercase(s):
    uppercount=0
    lowercount=0
    for i in s:
        if i.islower():
            lowercount+=1
        elif i.isupper():
            uppercount+=1
        else:
            pass
    print(uppercount)
    print(lowercount)
upperlowercase(s)
