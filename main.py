# 1) Создать переменную типа String
name = 'Panda'
# 2) Создать переменную типа Integer
paws = 4
# 3) Создать переменную типа Float
age = 6.5
# 4) Создать переменную типа Bytes
fur = bytes(0)
# 5) Создать переменную типа List
vaccine = ['annually', "17/10", 2, True]
# 6) Создать переменную типа Tuple
birthday = ('02.06', 6)
# 7) Создать переменную типа Set
Panda_data = {'name_Panda', 'age_6.5', 'paws_4'}
# 8. Создать переменную типа Frozen set
Panda_family = frozenset(['cat_Hankey', 'man_Kostya', 'women_Rezeda'])
# 9) Создать переменную типа Dict
Panda_friends = {'cat': 'Hankey',
                 'man': 'Kostya',
                 'dog': 'Kai'}
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(name), name, type(paws), paws, type(age), age, type(fur), fur, type(vaccine), vaccine, type(birthday), birthday, type(Panda_data), Panda_data, type(Panda_family), Panda_family, type(Panda_friends), Panda_friends)
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
dog = 'Panda'
cat = 'Mr.Hankey'
pets = {dog, cat}
print('pets: ', pets)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(name, age, sep=' ')
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(name + ' ' + str(age))