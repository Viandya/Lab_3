def f(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        f(a + 1, b)
    else:
        f(a - 1, b)


a = int(input())
b = int(input())
f(a, b)
print()
