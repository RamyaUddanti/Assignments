a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(a):
    return a[-1:]
def list_sorted(a):
    return sorted(a,key=last)
print(list_sorted(a))
