#This program give the Biges among 3 Numbers
#Bigex1.py
a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))
c=int(input("Enter Thired number:"))
if(a>b)and(a>c):
	print("Big ({},{},{})={}".format(a,b,c,a))
if(b>a)and(b>c):
	print("Big ({},{},{})={}".format(a,b,c,b))
if(c>a)and(c>b):
	print("Big ({},{},{})={}".format(a,b,c,c))
if(a==b)and(b==c):
	print("\n THERE IS NO BIG NUMBER ALL VALUES IS SAME")