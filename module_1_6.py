my_dict={"Иван": 1995, "Ольга": 1994, "Тимур": 1999, "Алина": 2001}
print(my_dict)
print(my_dict['Иван'])
print(my_dict.get('Вася'))
my_dict.update({"Гульнара": 1989, "Света": 1994})
print(my_dict)
name=input("Введите имя которое нужно удалить ") # Немного отошел от требований
a = my_dict.pop(name)
print(name, a)
print(my_dict)
# Задание 3
my_set={11, 25, 25, 11, 42, 63}
print(my_set)
my_set=set(my_set)
my_set.add(58)
my_set.add(89)
print(my_set)
deleted=my_set.pop()
print(my_set)
