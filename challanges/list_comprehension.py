#Hackerank  - https://www.hackerrank.com/challenges/python-lists/problem
def lists():
    N = int(input())
    lists = []
    for i in range (N):
        command = [(x) for x in input().split(" ")]
        if command[0] == "insert":
            lists.insert(int(command[1]),int(command[2]))
        if command[0] == "remove":
            lists.remove(int(command[1]))
        if command[0] == "append":
            lists.append(int(command[1]))
        if command[0] == "sort":
            lists.sort()
        if command[0] == "pop":
            lists.pop()
        if command[0] == "reverse":
            lists.reverse()
        if command[0] == "print":
            print(lists)


lists()