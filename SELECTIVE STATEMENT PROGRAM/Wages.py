name = input("Enter your name: ")
age  = int (input("Enter your age: "))
gen = input("Enter your gender (M or F): ")
if gen=="M":
    if age>=18 and age<30:
        print("Wages will be Rs 700 per day.")
    elif age >=30 and age <=40:
        print("Wages will be Rs 800 per day.")
elif gen == 'F':
    if age>=18 and age<30:
        print("Wages will be Rs 750 per day.")
    elif age >=30 and age <=40:
        print("Wages will be Rs 800 per day.")
