p=input("enter").split()
o= [int(e) for e in p]
n=tuple(o)
print(n)
even_no=0
odd_no=0
for i in n:
    if i%2==0:
        even_no+=1
    else:
        odd_no+=1
print("Number of even numbers:",even_no )
print("Number of odd numbers:",odd_no )
        