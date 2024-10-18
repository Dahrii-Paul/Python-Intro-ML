#print a table
def table():
	a=int(input("enter the no :"))
	b=int(input("enter table upto :"))
	for i in range(1,b+1):
		c=a*i
		print("%d * %d = %d"%(a,i,c))
