lst=map(int,input("enter elements in a list:").split())
def squares(n):
    return n*n
res=list(map(squares,lst))
print(res)