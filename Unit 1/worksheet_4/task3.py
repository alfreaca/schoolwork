outlet_1_sales = [10, 12, 15, 10]
outlet_2_sales = [5, 8, 3, 6]
outlet_3_sales = [10, 12, 15, 10]

for i in range(4):
    print("Total for quarter "+str(i+1), str(outlet_1_sales[i]+outlet_2_sales[i]+outlet_3_sales[i]))
