import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime - starttime
        print(f'czas wykonania funkcji: {wynik} s')
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper


@usypiacz
@pomiarczasu
def big_lista():
    sum([i**5 for i in range(10_000_000)])

big_lista()

def repeat(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeat(n=8)
def policz(x,y):
    print(f'wynik: {(x+y)**3}')

policz(1,4)

