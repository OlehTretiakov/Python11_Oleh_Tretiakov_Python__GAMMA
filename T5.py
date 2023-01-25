a = tuple(input().split())
b = tuple(input().split())
a = list(a)
for x in reversed(b):
    a.insert(2, x)
print(tuple(a))