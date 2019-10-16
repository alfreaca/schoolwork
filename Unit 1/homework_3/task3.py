sunshine = 0
maxHours = 0
minHours = 100
totalSunshine = 0

while True:
    sunshine = int(input("Input the sunshine: "))
    if sunshine > maxHours:
        maxHours = sunshine
    if sunshine < minHours:
        minHours = sunshine
    totalSunshine += sunshine
    if sunshine == -1:
        break

print("Max sunshine hours:", maxHours)
print("Min sunshine hours:", minHours)
print("Total sunshine hours:", totalSunshine)

