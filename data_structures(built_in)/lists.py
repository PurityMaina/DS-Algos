# a data structure that holds an ordered collection of values i.e you can store a sequence of values in a list
# are mutable

shopping_list = ['ndizi', 'maembe', 'nanasi']
print('I have', len(shopping_list), 'items to purchase')

print('These are the items')
for item in shopping_list:
    print(item)

print('I also have to buy machungwa')
shopping_list.append('machungwa')
print('My shopping list is now', shopping_list)

print('i actually have ndizi')
del shopping_list[0]
print('My current shopping list is', shopping_list)

