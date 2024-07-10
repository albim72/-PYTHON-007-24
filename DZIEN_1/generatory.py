#przykład1

def liczby():
    for i in range(21):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)
