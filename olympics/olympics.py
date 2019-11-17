import csv

exists = False
rows = []
event = input("Input the name of the event: ")
gender = input("Input the gender of the competitor: ")

time_h = float(input("Input the hours taken: "))
time_m = float(input("Input the minutes taken: "))
time_s = float(input("Input the seconds taken: "))

time = time_h*3600+time_m*60+time_s

with open('olympic_records.csv') as record_file:
    csv_reader = csv.reader(record_file, delimiter=",")
    for row in csv_reader:
        rows.append(row)

for row in rows:
    if event == row[0] and gender == row[1]:
        exists = True
        if time < float(row[2]):
            print(f"New record! the time was {time} seconds and is the new olympic record.")
            row[2] = str(time)
        else:
            print("Sorry not a new record")

if not exists:
    temp_lst = [event, gender, str(time)]
    rows.append(temp_lst)
    print("New record")
    print(rows)

with open('olympic_records.csv', 'w', newline='') as record_file:
    writer = csv.writer(record_file)
    for row in rows:
        writer.writerow(row)

