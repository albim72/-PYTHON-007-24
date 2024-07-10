#przykład1

def liczby():
    for i in range(21):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2
def wznowienie(n,k):
    print("wstrzymianie działanie")
    yield 1005
    print("wznowienie działania")

    print("wstrzymianie działanie")
    yield n+k
    print("wznowienie działania")

    n = 8*k - 2
    print("wstrzymianie działanie")
    yield n-k
    print("wznowienie działania")

    print("wstrzymianie działanie")
    yield n*k
    print("wznowienie działania")

    print("wstrzymianie działanie")
    yield n/k
    print("wznowienie działania")


print(wznowienie(6,8))
print(list(wznowienie(6,8)))

print("_"*50)
for i in wznowienie(6,8):
    print("*"*40)
    print(type(i))
    print(f'zwrócowno wartośc {i}')

#przykład 3

def generator():
    x=0
    while True:
        y = yield x
        # z = yield x
        if y is None:
            x = x+1
            # z = x - 7
        else:
            x=y*3
            # z = z+5

g = generator()

print("_"*50)
print(next(g))
print(next(g))
print(next(g))
print(g.send(121))
# print(g.send(y=888))
print(next(g))
print(next(g))
print(g.send(73))
