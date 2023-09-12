#write the program that detrmines whether a yearentered by the useris a leap year or not using if- elif-else statements.

def isLeapYear(year):
 if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
   return True
 else:
   return False

year = int(input("Enter a year :"))

if isLeapYear(year):
  print('{} is not a leap year.'.format(year))