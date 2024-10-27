a = [1, 2, 3, 4, 5]
b = a[2]
c = b + len(a)
print(a)
print(b)
print(c)

spisok = [1, 2, 3, 4]
spisok.append(5)
spisok.insert(2, 'python')
print(spisok)

user = {'name':'slava', 'age':'28', 'skills':["Python"]}
print(user)
user["skills"] = ['Python','Django']
print(user)

user = {}
user['name'] = 'Слава'
user['age'] = 28
user['skills'] = ['Python']
print(user)
user['skills'].append('Django')
print(user)
