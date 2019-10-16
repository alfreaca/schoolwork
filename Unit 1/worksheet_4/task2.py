search_name = input("Input the name you want to search for: ")

name = ['name1', '1', 'name2', '2', 'name3', '3', 'name4', '4']
max_elements = len(name)
name_in_array = False

for i in range(max_elements):
    if name[i] == search_name:
        print("FOUND! ID Number:", name[i+1])
        name_in_array = True
        break

if not name_in_array:
    print("name not found")
