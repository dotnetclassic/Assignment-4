#Using conditional statements, check if the number is:

# - Even or Odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#  - Positive, Negative, or Zero.
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
if number % 2 == 0 and number % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif number % 2 == 0:
    print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 2 or 3.")


#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."

age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Do you have a nationality of 'Pakistani' (yes/no): ")
    if nationality.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote.")  
                        
# Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), 
# teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)

age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
#  - Check if a year is a leap year or not    
month = int(input("Enter a month (as a number between 1 and 12): "))
if month == 2:
    print("The month has 28 days.")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("The month has 30 days.")
else:
    print("The month has 31 days.")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

