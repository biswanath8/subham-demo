#This accept number of a week and display it's name
#WEEK.py
a=int(input("Enter any number:"))
if(a==1):
	print("{} is SUNDAY".format(a))
elif(a==2):
	print("{} is MONDAY".format(a))
elif(a==3):
	print("{} is TUESDAY".format(a))
elif(a==4):
	print("{} is WEDNESDAY".format(a))
elif(a==5):
	print("{} is THURSDAY".format(a))
elif(a==6):
	print("{} is FRIDAY".format(a))
elif(a==7):
	print("{} is SATURDAY".format(a))
else:
	print("\n THIS IS NOT IN THE WEEK")