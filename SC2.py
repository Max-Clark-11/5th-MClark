#Name: Max Clark
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

Height = int(input("Put in your height (in inches):"))
Weight = int(input("Put in your weight (in pounds):"))
MathHeight = Height * Height

BMI = Weight/MathHeight * 703

if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI < 25:
    print("You are normal weight")
elif BMI >= 25 and BMI < 30:
    print("You are overweight")
else:
    print("You are obese")
print(BMI)