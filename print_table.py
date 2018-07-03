#Accepts a dictionary as an input, outputs the contents as a rich table

def print_table(user_dict, col_1, col_2):
    import html
    #Create a list of lists for the dictionary
    table_data = [[col_1, col_2]]
    for key in user_dict:
        table_data.append([key, dict[key]])
    print(table_data)

reaction = {
"H20":20,
"CH4":30,
"O2":10,
"CO2":40,
}

print_table(reaction,"Species","Percentage")
