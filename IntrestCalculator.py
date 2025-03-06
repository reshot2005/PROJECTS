principle = 0
rate = 0
time = 0
principle = float(input("Enter the Principle Value :"))
rate = float(input("Enter the rate Value :"))
time = int(input("Enter the time Value :"))
while principle <= 0:
    print("Principle Value cannot be Zero")
    principle = float(input("Enter tha Principle Value: "))

while rate <= 0:
    print("rate Value cannot be Zero")
    rate = float(input("Enter tha rate Value: "))

while time <= 0:
    print("time Value cannot be Zero")
    time = float(input("Enter tha time Value: "))

total = principle * pow((1 + rate / 100), time)

print(f"Balace after the Calculation is {total:.2f}rs")