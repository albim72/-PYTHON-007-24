from pojazd import Pojazd

pj = Pojazd()
odl = 578
jd = 52
cn = 6.48

print(f'spalanie [l/100km]: {pj.spalanie(odl,jd):.3f}')
print(f'koszty przejazdu na trasie {odl} km -> {pj.kosztyprzejazdu(odl,jd,cn):.2f} zł')
