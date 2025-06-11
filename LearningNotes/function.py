def myfunction(first, last): 
    print(f"hello {first} and hello {last}")
    # default return None
    
myfunction("amy", "lin")


def printToFile(message):
    file = open("write.txt", "w")
    file.write(message)

    
printToFile("hello")


def increment(num, by = 1):
    return num + by

print(increment(2))    # default parameter 1
