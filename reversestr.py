str_rev=""
def rev(i,string):
    global str_rev
    str_rev=i+str_rev
    return str_rev


string="1234abcd"
for i in string:
    r=rev(i,string)
print(r)