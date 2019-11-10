isbn_num = input("The modulo 10 system is a type of checksum, to see how it works, input an ISBN number: ")
isbn_lst = list(isbn_num)
isbn_multi = [0]*12
weightings = "131313131313"
weightings_lst = list(weightings)
total = 0

isbn_multi[0]
for i in range(len(isbn_lst)-1):
    isbn_multi[i] = str(int(isbn_lst[i]) * int(weightings[i]))

print("="*60+"\n"+"ISBN NUM:   "+isbn_num+"\n"+"="*60+"\n"+"Weightings: "+weightings+"\n"+"="*60)
print("Multiplication: "+", ".join(isbn_multi))

for i in range(len(isbn_multi)-1):
    total += int(isbn_multi[i])

print("="*60+"\nAddition: "+str(total))
print("="*60+"\nRemainder when divided by 10: "+str(total%10))
print("="*60+"\nSubtraction from 10: "+str(10-total%10))
print("="*60+"\nFinal check digit: "+str(10-total%10)+"\n"+"="*60)
