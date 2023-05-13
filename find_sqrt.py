import math as m
# p = float(input("Podaj liczbe pod pierwsiatkiem: "))
# e = float(input("Podaj z jaka dokladnoscia ma obliczyc: "))
# l = float(input("Podaj maksymalna liczbe iteracji petli: "))

# a = p
# i = 0 

# while m.fabs(a-(p/a))>e and i<l:
#     a=0.5*(a+(p/a))
#     i+=1
# print(a)
# print(m.sqrt(p))


a = float(input('Podaj liczbe pod pierwiastkiem: '))
n = float(input('Podaj stopien pierwiastka: '))
e = float(input('Ilosc iteracji: '))

xo=a
i=0

while i<e:
    xo=(1/n)*((n-1)*xo+(a/(xo**(n-1))))
    i+=1
print(xo)