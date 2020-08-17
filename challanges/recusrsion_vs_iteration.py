#calling sum recusrsively

def sum(n):
    if n<=0 :
        return 0
    return n + sum(n-1)


#calling sum iteratively
def summ(n):
    while (n != 0):
        summed = (n) + (n-1)
        return summed
