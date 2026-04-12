countries=['Nepal','Iran','Poland','Finland','Nederland','Japan','China']
sub_string="land"
matching_lst=[x for x in countries if sub_string in x]
print("countries are:",countries)
print("countries containig substring land:",matching_lst)