#body mass calculator
print("This is Body Mass Calculator,You have to Put your Measurements below\n")
height = float(input("What is Your Height?\n"))
weight = float(input("What is your weight?\n"))
bmi = (weight/height**2)*10000

print("Your Body mass Index is ---- ",bmi)
input("\n")
		
		
print("Underweight = <18.5")
print("Normal weight = 18.5–24.9") 
print("Overweight = 25–29.9") 
print("Obesity = BMI of 30 or greater")
input("bingo")
  