def kwadratowa(a,b,c):
	delta = b**2 - 4*a*c
	if (delta<0):
		return []
	sqrt_delta = delta**(1/2)
	x1 = (-sqrt_delta - b)/(2*a)
	x2 = (+sqrt_delta - b)/(2*a)
	return [x1,x2]
