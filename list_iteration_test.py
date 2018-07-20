my_data = [["Species", "Percentage"]["H20",50]["CO2",50]]
my_table = []

for i in my_data:
    for j in my_data[i]:
        my_table.append(my_data[i][j])

print (my_data)
print (my_table)
