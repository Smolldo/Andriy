# tuple - кортеж
new_tuple = ()
tuple1 = (1, 2, 3, 4, 'book', True)

#  Створіть два кортежі, кожен з яких містить назву продукту, його вагу в грамах та ціну в гривнях.
mac1 = ('apple', 10000, 170)
mac2 = ('banana', 49000, 630)

#  Створіть список кортежів, де кожен кортеж містить назву книги та рік її видання. 
# Виведіть назви всіх книг та їх роки видання.

books = [('Ultimate python Hola Mundo', 2024), ('Guia', 2024), ('Minecraft', 2023)]
# print(books)

# set - множина 

empty_set = set()

set1 = {'apple', 'banana'}
# print(set1)

nums = set([1,2,3,4,4,5,6,7,7,7,7])

#add - додає новий елемент в множину
nums.add(10)

# print(nums)

#remove - видалає елемент якщо він є.
nums.remove(6)

# nums.remove(12)  - виникає помилка, якщо об'єкта немає в множині.

# print(nums)

#discard - видаляє елемент. якщо його немає, помилку не видає

nums.discard(5)

nums.discard(12)

# print(nums)

#pop - видаляє рандомний елемент множини

elem = nums.pop()
elem1 = nums.pop()
elem2 = nums.pop()
# print(nums)

# print(elem)
# print(elem1)
# print(elem2)




# Створіть множину з унікальних чисел від 1 до 5, використовуючи функцію set(). 
# Потім додайте до неї число 6 
# і видаліть число 3. 
# Виведіть результуючу множину.

num2 = set([1, 2, 3, 4, 5])
num2.add(6)
num2.discard(3)
# print(num2)


#СЛОВНИКИ

dictionary = {}

person = {
    'name': 'John',
    'age': 43,
    'city': 'Berlin'
}

# print(person['age'])
# print(person['city'])

#get - отримати значення за ключем, якщо такого немає - виводить повідомлення(None)
# print(person.get('BMW', 'no such key'))

person = {
    'name': 'John',
    'age': 43,
    'city': 'Berlin'
}

#додавання нового елементу до словника
person['car'] = 'BMW'
print(person)
person['car'] = 'Mercedes'
print(person)
#del (delete) - видаляє пару ключ-значення

# del person['car']
# print(person)


#перебір словника keys() - виводить лише ключі. values() - виводить тільки значення

# print(person.keys())
# print(person.values())


# pop() - видалення пари за ключем. якщо немає пари - повертає None


person.pop('age')
print(person)

p = person.pop('school', 'No school')
print(p)
print(person)






friends = {
    'Valeriy': {
        'street': 'Pivdenna',
        'city': 'SNK',
        'index': 57301
    },
    'Alex': {
        'street': 'Karpenka',
        'city': 'Ternopil',
        'index': 46002
    },
}
print(friends['Alex']['street'])