def get_headings(csv):
    csv = [heading.strip() for heading in csv.split(",")] 
    return csv

print(get_headings("name,age,city"))

headins = get_headings("name,age,city")
print(headins)

print(get_headings("first name,last name,phone"))

print(get_headings("username , email , signup date "))