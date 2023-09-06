year=2000
if(year % 400 ==0) and (year % 100 ==0):
  print("{0} is a leap yaer".format(year))
elif(year % 4==0) and (year % 100 !=0):
   print("{0} is a leap yeae".format(year))
else:
   print("{0} is not a leap year".format(year))
