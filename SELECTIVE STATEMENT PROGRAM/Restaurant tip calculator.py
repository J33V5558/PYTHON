print("RESTAURANT TIP CALCULATOR.")
fr=int(input("Enter food rating (1-5): "))
sr = int(input("Enter Service rating (1-5): "))
ar =int(input("Enter ambience rating (1-5): "))
am =int(input("Enter bill amount (1-5): "))
if fr in [4,5]:
    if sr in [4,5] and ar in [4,5]:
        print(f"Tip will be Rs {am*(10/100)}")
    elif sr in [1,2,3] and ar in [1,2,3]:
        print(f"Tip will be Rs {am*(5/100)}")
elif fr in [1,2,3]:
    if sr in [4,5] and ar in [4,5]:
        print(f"Tip will be Rs {am*(5/100)}")
    elif sr in [1,2,3] and ar in [1,2,3]:
        print(f"Tip will be Rs {am*(1/100)}")
