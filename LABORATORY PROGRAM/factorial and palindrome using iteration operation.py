n = int(input("Enter a number: "))
if n%2!=0:
    f=1
    for i in range(1,n+1):
        f *=i
    print(f"The factorial is {f}")
    print(f"Digits of the factorial number is {len(str(f))}")
elif n%2==0:
    if str(n) == str(n)[::-1]:
        print("The given number is in palindrome.")
    else:
        print("The given number is not in palindrome.")
