#import datetime
#my_date = datetime.datetime(2020, 11, 15, 14, 19, 45)
#print('The date is: {:%B %d, %Y}'.format(my_date))

# March 21 fell on Tuesday and it is 61st day of the year.

# list[start:end:step]

#print('{0:%B %d, %Y} fell on {0:%A} and it is {0:%j} st day of the year'.format(my_date))
# print(help(str.format))

# person = {'name': 'Jenn', 'age': 23}
# print('dictionary values{name} and {age}'.format(**person))
# tup = ('Jenn', 23)
# print('My name is {0[0]} and age is {0[1]}'.format(tup))

# for i in range(1, 11):
#   print('The value is {:04}'.format(i))


# class Person():

#   def __init__(self, name, age):
#       self.name = name
#       self.age = age


# p1 = Person('Jack', '33')
# sentence = 'My name is {0.name} and age is {0.age}'.format(p1)
# print(p1.age)
# print(sentence)
#import random
#course = ['History', 'Physics', 'Chemistry', 'Math', 'Econony']
# for items in course:
#    print(items)
# if True:
#    print("This is working")
#course_value = random.choice(course)
# print(course_value)
#import datetime
#today_date = datetime.date.today()
# print(today_date)
items = [("product1", 10), ("product2", 15), ("product3", 13)]
print(items[1])

items.sort(key=lambda item: item[1])  # lambda parameter:expression
#x = list(map(lambda item: item[1], items))
x = [item[1] for item in items]  # expression for item in items condition
#y = list(filter(lambda item: item[1] > 10, items))
y = [item[1] for item in items if item[1] > 10]
mylist = [item for item in range(1, 11) if item % 2 == 0]
mylist1 = list(filter(lambda item: item % 2 == 0, range(1, 11)))
# print(mylist1)
# print(x)
# print(y)
mylist = []
# for letter in 'abcd':
# for num in range(4):
#    mylist.append((letter, num))

mydict2 = {'a': 3, 'b': 4, 'c': 5, 'c': 6}
mylist = [(letter, num) for letter in 'abcd' for num in range(4)]
print(mylist)

mydict = {key: value for key, value in mylist}
print(mydict)
print(mydict2)
