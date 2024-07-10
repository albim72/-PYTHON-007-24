print("programowanie funkcyjne")
#funkcja wyższego rzędu
def witaj(imie):
    return f'Miło Cię widziec {imie}!'

def konkurs(punkty,miejsce,imie):
    return f'uczestnik konkursu {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'

def osoba(funkcja,*args,**kwargs):
    return funkcja(*args,**kwargs)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,56,24,"Anna"))

#przykład 2 - prosty dekorator

def startstop(funkcja):
    def wrapper(*args):
        print("_"*50)
        print("startowanie funkcji...")
        funkcja(*args)
        print("kończenie funkcji...")
    return wrapper


def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)
zw("czekoladek")


@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na torcie urodzinowym')

dmuchanie("świeczek")

@startstop
def policz(x,y):
    print(f'wynik: {(x+2)/y}')



policz(34,7.88)
