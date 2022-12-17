# liczby zaprzyjanione
# funkcje sp i sp2 licza sume dzielników

def sp(n):
	s=0
	for p in range(1, n//2+1):
		if n%p==0:
			s=s+p
	return s
#end

def sp2(n):
	s=1
	p=2
	while p*p<n:
		if n%p==0:
			s=s+p+n//p
		p+=1
	if p*p == n:
		s=s+p
	return s



for n in range(1, 10_000):
	k=sp2(n)
	if(n) == sp2(k) and n < k:
		print(n,k)

print("koniec")