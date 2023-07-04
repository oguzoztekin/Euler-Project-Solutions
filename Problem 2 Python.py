#Problem 2
def Problem2():
	sum=0
	x=1
	y=2
	while x<=4000000:
		if x%2==0:
			sum+=x
		x,y=y,x+y
	print(sum)
