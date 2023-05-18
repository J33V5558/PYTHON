s1 = int(input("Enter side 1 (in cm): "))
s2 = int(input("Enter side 2 (in cm): "))
s3 = int(input("Enter side 3 (in cm): "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("Triangle formation is possible.")
else:
    print("Trinangle formation is impossible.")
