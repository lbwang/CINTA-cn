#Input, two integer x and y with n-bits, Python version
#Output, xy
def fast_mul(x, y):
    maxlen = 8
    n = max(x.bit_length(), y.bit_length())
    if n < maxlen:
        return x * y
    m = n / 2              #floor of n
    x1, x2 = leftmost(x, m), rightmost(x, m)
    y1, y2 = leftmost(y, m), rightmost(y, m)
    t1 = fast_mul(x1, y1)
    t2 = fast_mul(x2, y2)
    t3 = fast_mul(x1 + x2, y1 + y2)
    t4 = t3 - t1 - t2
    return (t1 << (2*m)) + (t4 << m) + t2

#Actually, function leftmost does not always
#return the leftmost significant m bits.
def leftmost(x,m):
    n = x.bit_length()
    if n > m:
        return x >> m
    else:
        return 0

def rightmost(x,m):
    n = x.bit_length()
    if n > m:
        return ((1 << m) - 1) & x
    else:
        return x

#Sage version
def fast_mul(x, y):
    maxlen = 8
    n = max(x.ndigits(), y.ndigits())
    if n < maxlen:
        return x * y
    m = n // 2              #floor of n
    x1, x2 = leftmost(x, m), rightmost(x, m)
    y1, y2 = leftmost(y, m), rightmost(y, m)
    t1 = fast_mul(x1, y1)
    t2 = fast_mul(x2, y2)
    t3 = fast_mul(x1 + x2, y1 + y2)
    t4 = t3 - t1 - t2
    return (t1 << (2*m)) + (t4 << m) + t2

#Actually, function leftmost does not always
#return the leftmost significant m bits.
def leftmost(x,m):
    n = x.ndigits()
    if n > m:
        return x >> m
    else:
        return 0

#return the rightmost m bits
def rightmost(x,m):
    n = x.ndigits()
    if n > m:
        return ((1 << m) - 1) & x
    else:
        return x

# Function to extract k bits from p position
# and returns the extracted value as integer
def bitExtracted(number, k, p):
    return ( ((1 << k) - 1)  &  (number >> (p-1) ) );

#Without bit operations version
def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2

		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)

		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
