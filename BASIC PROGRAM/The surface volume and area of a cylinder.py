r =float(input("Enter Radius(CM): "))
h = float(input("Enter Height(CM): "))
vol = 3.14*r*r*h
sur = ((2*3.14*r)*h)+((3.14*r**2)*2)
print(f'Surface : {sur}cm^2 and Volume : {vol}cm^3')
