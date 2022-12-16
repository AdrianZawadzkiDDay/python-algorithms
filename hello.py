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

def sp(n):
	s=0
	for p in range(1, n//2+1):
		if n%p==0:
			s=s+p
	return s
#end

for n in range(1,10000):
	if sp2(n) == n:
		print(n)