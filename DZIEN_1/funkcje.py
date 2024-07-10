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
