from math import sqrt

print ('Dla równania kwadratowego ax2+bx+c=0')
a=float(input('Podaj a: '))
b=float(input('Podaj b: '))
c=float(input('Podaj c: '))
delta=(b*2)-(4*a*c)

print("delta:", delta)

if delta > 0:
	p=sqrt(delta)
	x1=(-b-p)/(2*a)
	x2=(-b+p)/(2*a)
	print(f'x1={x1:0.2f} \n x2={x2:0.2f}')
elif delta == 0:
    x0 = -b/(2*a)
    print ("x0 = "), x0
else:
    print ("brak rozwiązań")
	
