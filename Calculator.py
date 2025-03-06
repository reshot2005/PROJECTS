operator = input("+ , - , * , / :")
n1 =  float(input("Enter the Fist Number To Calculate:" ))
n2 = float(input ("Enter the Second Number To Calculate :"))
if operator == "+":
    result = n1 + n2
    print(result)
elif operator == "-":
    result = n1 - n2
    print(result)
elif operator == "*":
    result = n1 * n2
    print(result)
elif operator == "/":
    result =  n1 / n2
    print(round(result , 3))

else :
    print(f"{operator} is Invalid Selection")
