
def fact(x):
    if x!=0: 
        return x*fact(x-1)
    else:
        return 1

print(fact(10))
print(fact(4))
print(fact(2))