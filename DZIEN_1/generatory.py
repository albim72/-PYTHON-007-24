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
