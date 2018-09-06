def d2b(x):#带浮点十进制转二进制
	print(isinstance(x,int))
	if isinstance(x,int):
		print(bin(x)[2:])
		return int(bin(x)[2:])
	else:
		x_float=x-int(x)
		bins=''
		while x_float:
			x_float *= 2
			bins+='1' if x_float>=1. else '0'
			x_float -= int(x_float)
		print(int(bin(int(x))[2:])+float('.'+bins))
		return float(int(bin(int(x))[2:])+float('.'+bins))
def b2d(x):#带浮点二进制转十进制
	if isinstance(x,int):
		print(int(str(x),2))
		return int(int(str(x),2))
	else:
		x=float(x)
		t=str(x).replace('.','')
		s=0
		j=0
		for i in t:
			s+=int(i)*2**(str(x).index('.',0)-j-1)
			j+=1
		print(s)
		return float(s)
d2b(.5)
b2d(.1101)
