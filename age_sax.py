age=int(input("enter the any age"))
sex=input("enter the any sex")
if sex=="female":
	print("urbon areas")
elif sex=="male":
	if age>=20 and age<=40:
			print(" work anywhere area")
	elif age>=40 and age<=60:
		     print("only urban area")
	else:
  	   print('error')
else:
 print("error")