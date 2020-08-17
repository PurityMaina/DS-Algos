#Implement an algorithm to determine if a string has all unique characters.

def unique(n):
    temp = []
    for i in range(len(n)):
        for j in range(1+1, len(n)):
            if(n[i] == n[j]):
                print("The String ", n, " has duplicate characters",  temp)
                return False
        temp.append(n[j])
        print("The String ", n, " has all unique characters", temp)
        return True

#n = "wahddhdbchbhdfieiuwihjfk"
n = "njerima"
unique(n)
