import random

print("gra")
a=1
b=100
x=random.randint(1, 100)
y=0
i=0
while x!=y:
	i=i+1
	y=(a+b)//2
	
	print("y:",y)
	if y<x:
		print("za mało")
		a=y
	elif y>x:
		print("za dużo")
		b=y
		

print("Wygrana")
print("liczba prób: ", i)
 

