#Enter 2 int numbers find the bigest number
#BIGEx2.py
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if(a>b):
	print("Big({},{})={}".format(a,b,a))
else:
	print("{} is Big".format(b))