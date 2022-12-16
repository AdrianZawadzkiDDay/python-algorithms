from random import randint

print("urodziny")

for k in range(1, 50):
	licz=0
	for i in range(1000):
		t={}
		for i in range(1,366): t[i]=0

		for i in range(k):
			dz=randint(1, 365)
			t[dz]=t[dz]+1

		b=False
		for i in range(1, 366):
			if t[i]>1 : b=True
			
		if b: licz+=1

	print(k, licz/10)