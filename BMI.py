print("\tBMI CALCULATOR ")
height = float(input ("Enter your height in meters : "))
weight = float(input("Enter your weight in kgs : "))
bmi = weight/(height * height )
if bmi<18 and bmi >0 :
 category = "underweight"
elif bmi>18 and bmi <24 :
    category = "fit"
elif bmi >24 and bmi < 29 :
    category = "overweight"
else : 
    category = "obese"

print(f"Your BMI is {bmi}")
print(f"You are classified as {category}")
