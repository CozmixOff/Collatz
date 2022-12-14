m = int(input('Choissez un nombre entier strictement supérieur à 0 :\n'))
n = m
x = 0
while not n == 1:
    x += 1
    if n%2 == 0:
        n = int(n/2)
    elif n%2 == 1:
        n = 3*n+1
    print ('['+str(x)+'] '+str(n))
print('\n\nEn suivant la conjecture de Collatz, le nombre '+str(m)+' atteint 1 en '+str(x)+' ittérations.')