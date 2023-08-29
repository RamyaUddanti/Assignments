list=map(int,input("elements in a list").split())
def sumoflist():
    sum=0
    for i in list:
        sum=sum+i
        i+=1
    print(sum)
sumoflist()
