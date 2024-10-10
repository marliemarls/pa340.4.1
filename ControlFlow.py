# Question 1: 
# x = 7
# if x < 10:
#     print("Less than 10")

#Question 2: 
# x = 15
# if x < 10:
#     print("Less than 10")
# elif x > 10: 
#     print("Greater than 10")

#Question 3: 
# x = 15
# if x < 10:
#     print("Less than 10")
# elif x > 10: 
#     print("Greater than 10")
# elif x > 10 and x < 20:
#     print("Between 10 and 20")
# elif x > 20 or x == 20:
#     print("Greater than or equal to 20")


#Question 4: 
# x = 15
# if x < 10 and  :
#     print("Less than 10")
# elif x > 10: 
#     print("Greater than 10")


#Question 5: 
grade = int(input("Input a numerical grade between 0-100: "))
if grade == 0:
    print("Score out of range.")
elif grade < 60:
    print("F")
elif grade < 70: 
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
elif grade <= 100:
    print("A")

#Question 6:
filing_status = input("Please input your filing status: (Single, Married Filing Jointly, Qualifying Widower, Married Filing Separately, OR Head of Household)")
income = int(input("Please input your annual income: "))

if filing_status == "Single" and income <= 8350:
    print("Tax rate is 10%")
elif filing_status == "Single" and income <= 33950:
    print("Tax rate is 15%")
elif filing_status == "Single" and income <= 82250:
    print("Tax rate is 25%")
elif filing_status == "Single" and income <= 171550:
    print("Tax rate is 28%")
elif filing_status == "Single" and income <= 372950:
    print("Tax rate is 33%")
elif filing_status == "Single" and income > 372950:
    print("Tax rate is 35%")

