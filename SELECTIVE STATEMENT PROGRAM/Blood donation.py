name = input("Enter your name: ")
age = int(input('Enter your age: '))
w=  int(input("Enter your weight: "))
if age>18 and w>40:
    print(f"{name} is eligible!")
else:
    print(f"{name} is not eligible!")
