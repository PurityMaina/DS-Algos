# LIFO data structure
# Add an item to the top of the stack, use append().
# To retrieve an item from the top of the stack, use pop() without an explicit index


def createStack():
    pancakes =[]
    return pancakes

def isEmpty(pancakes):
    return len(pancakes) == 0
    #I ate the entire plate


def push(pancakes, item):
    pancakes.append(item)
    print('Straight up from the pan',pancakes)


def pop(pancakes):
    if isEmpty(pancakes):
        return -1, print('No pancakes left, we cleared the plate sis')
    pancakes.pop()
    print('I got too full, did not have the last one', pancakes)


def isTop(pancakes):
    if isEmpty(pancakes):
        return -1
    return pancakes[len(pancakes)-1], print('The warmest pancake is the', pancakes[len(pancakes)-1])

pancakes = createStack()
push(pancakes, str('1st pancake'))
push(pancakes, str('2nd one'))
push(pancakes, str('3rd pancake'))
isEmpty(pancakes)
isTop(pancakes)
pop(pancakes)

