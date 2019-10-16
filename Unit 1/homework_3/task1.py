smallest = 'z'
largest = 'a'

for i in range(4):
    letter = input("Input a letter: ")
    if letter < smallest:
        smallest = letter

    if letter > largest:
        largest = letter

print("largest:", largest)
print("smallest:", smallest)
