open_list = ["("]
close_list = [")"]

def bracket_match(text):
    stack = [] # store in temp loc
    diffCounter = 0
    ans = 0

    for i in range(0, len(text)):   # traverse
        if text[i] in open_list:  # find opening bracket and closing bracket
            stack.append(i)
            diffCounter += 1
            print("Appending",len(stack))
        elif text[i] in close_list and len(stack) > 0:  #find close for opening bracket
            stack.pop()
            diffCounter -= 1
            print("Popping", len(stack))
        if ( diffCounter < 0 ):
            diffCounter += 1
            ans += 1
    return ans  + diffCounter

print(bracket_match("(())"))