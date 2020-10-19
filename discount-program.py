Age = int(input("Enter your age: "))

if Age >= 60:
   print ('You are eligible for our 10% off senior discount!')
elif 18 <= Age < 60:
   print ('You are not eligible for the senior discount, but here is 5% off on us.')
else:
   print ('Sorry, you must be 18 to receive a discount')