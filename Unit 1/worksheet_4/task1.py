total = 0
numbers = [0]*5

for i in range(5):
    numbers[i] = int(input("Input a number: "))
    total += numbers[i]

print(list(reversed(numbers)))
print(total)
print(total/5)
