triangle1=int(input("enter the any triangle"))
triangle2=int(input("enter the any triangle"))
triangle3=int(input("enter the any triangle"))
if triangle1==60 and triangle2==60 and triangle3==60:
	print("it is equilateral")
elif triangle1==60 and triangle2==60 and triangle3==50:
	print("isosceles")
else:
	print("scalene")