Age = int(input("Enter your age: "))

if Age >= 60:
   print ('You are eligible for our 10% off senior discount!')
elif 18 <= Age < 60:
   print ('You are not eligible for the senior discount, but here is 5% off on us.')
else:
   print ('Sorry, you must be 18 to receive a discount')


"""
Important concepts: 

elif conditions are checked if previous conditions were false

**when using input(), they are strings by default - must define type as done in line 1

if-else or if-elif makes decisions based on conditions being true or false;  while loops
on the other hand will repeat certain parts of code until conditions are met  

"""

