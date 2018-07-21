class PrintTable(object):
    def __init__(self, user_dict):
        self.user_dict = user_dict
    def _repr_html_(self):
        return '<h1>'+str(self.user_dict)+'</h1>'

reaction = {
"H20":20,
"CH4":30,
"O2":10,
"CO2":40,
}

my_table = PrintTable(reaction)

print(my_table._repr_html_())
