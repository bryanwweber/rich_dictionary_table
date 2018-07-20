class PrintTableClass(object):
    def __init__(self, user_dict):
        self.user_dict = user_dict
    def __repr_html__(self):
        return '<h1>'+str(self.user_dict)+'</h1>'

reaction = {
"H20":20,
"CH4":30,
"O2":10,
"CO2":40,
}

my_table = PrintTableClass(reaction)

my_table
