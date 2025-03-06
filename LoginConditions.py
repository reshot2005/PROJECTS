useraname = input("Enter a Usrname:")

if len(useraname) > 12 :

    print("Do NOT exceed more than 12 Character")
elif not useraname.find(" ") == -1:
    print("!!Your USERNAME Should NOT Contain Spaces ")
elif useraname.isalpha():
    print("Username Cant Contain NUMBERS")

else:
    print(f"You a re Welcome {useraname}")