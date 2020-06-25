# these are key value pairs
# similar to hash or maps in other languages
# keys are immutable(int,str,tuple,float,boolean), values are mutable(list,set,array,dict)
# key-value pairs in a dictionary are not ordered in any manner

stack_operations = {
    'push': 'insert element onto topmost stack - time complexity of 0(1)',
    'pop': 'remove the topmost item from stack - time complexity of 0(1)',
    'isEMpty': 'check if stack is empty - time complexity of 0(1)',
    'isTop': 'check item at the top of the stack - time complexity of 0(1)',
    'size': 'returns the size of the stack - time complexity of 0(1)'
}
print('The second value of the dict is:', stack_operations['pop'])

del stack_operations['pop']
print('Dropped an operation, now we have {} operations', len(stack_operations))

stack_operations['pop'] = 'remove the topmost item from stack - time complexity of 0(1)'
print('Added an operation, now we have {} operations', len(stack_operations))

for key, value in stack_operations.items():
    print('This is what  a {} does {}'.format(key, value))
