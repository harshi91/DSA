def fact(n):
    print(n)
    if n<=1:
        return 1
    c=n*fact(n-1)
    return c
print(fact(5))
