#munu2.py
import sys
while True:
    print(("*")*30)
    print("Menu Driven for u program--->")
    print(("*")*30)
    print("\t1.sum")
    print("\t2.sub")
    print("\t3.mul")
    print("\t4.div")
    print("\t5.mod")
    print("\t6.expo")
    print("\t7.exit")
    ch=int(input("Enter u coice---->"))
    match ch:
        case 1:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("sum({}and{})={}".format(a,b,a+b))
        case 2:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("sub({}and{})={}".format(a,b,a-b))
        case 3:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("mul({}and{})={}".format(a,b,a*b))
        case 4:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("div({}and{})={}".format(a,b,a/b))
        case 5:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("mod({}and{})={}".format(a,b,a%b))
        case 6:
            a=float(input("Enter a value:"))
            b=float(input("Enter b value:"))
            print("expo({}and{})={}".format(a,b,a**b))
        case 7:
            sys.exit()
        case _:
            print("Invalit opction-->")
    
