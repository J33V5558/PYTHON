salary = float(input("Enter your salary (Rs): "))
year = float(input("Enter the year of service: "))
if year>10:
    print(f"Your bonus will be Rs{salary*(10/100)}")
elif year>6 and year<10:
    print(f"Your bonus will be Rs{salary*(8/100)}")
else:
    print(f"Your bonus will be Rs{salary*(5/100)}")
    
