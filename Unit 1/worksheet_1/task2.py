number = int(input("Input a three digit number: "))

print(str(number//100)+" Hundreds")
remainder = number%100

print(str(remainder//10)+" Tens")
remainder = remainder%10

print(str(remainder//1)+" Units")