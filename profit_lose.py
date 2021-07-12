cp=int(input("enter the  cp = "))
sp=int(input("enter the sp = "))
if sp>cp:
	print(sp-cp,"profit") 
elif sp<cp:
	print(cp-sp,"lose")
else:
	print("no lose no profit")