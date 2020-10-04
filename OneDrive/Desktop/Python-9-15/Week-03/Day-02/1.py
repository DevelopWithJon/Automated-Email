items = [1, 2, 3]
items.append(10)
print(items)

name_tuple = ("Suresh", "bob", "Vonn")
#name_tuple[1] = "Melv"
print(name_tuple.count("Suresh"))
print(name_tuple.index("bob"))

student_suresh = {
        'name': 'bob',
        'class': ('p', 'v', 'dsvs'),
        'grade': (100, 90, 95),
        'is_student': True,
        'name': 'ds'}

print(student_suresh.iloc[1])vendor

for i,v in student_suresh.items():
    print(i.index, v)
    
    