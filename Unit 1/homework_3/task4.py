sunshine = 0
maxHours = 0
minHours = 100
totalSunshine = 0

sunshine = int(input("Input the sunshine: "))
while sunshine != -1:
    if sunshine > maxHours:
        maxHours = sunshine
    if sunshine < minHours:
        minHours = sunshine
    totalSunshine += sunshine
    sunshine = int(input("Input the sunshine: "))

print("Max sunshine hours:", maxHours)
print("Min sunshine hours:", minHours)
print("Total sunshine hours:", totalSunshine)

