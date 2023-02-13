#! /usr/bin/python
print("Welcome to root calculator. To calculate roots of equation x2 + bx + c = 0, you have to enter b and c")

b = int(input("Enter b:"))
c = int(input("Enter c:"))

#delta evaluater
delta = (b**2) - (4*c)

#check if roots are real
if delta >= 0:
	#root evaluater
	root1 = ((-b)-(delta ** 0.5))/2
	root2 = ((-b)+(delta ** 0.5))/2

	print("""First root is {1},
Second root is {0}""".format(root2,root1))
else:
	print("There is not any real roots")


