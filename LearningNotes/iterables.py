print(type(range(5)))   # <class 'range'>


for i in "python":      # string is an iterable
    print(i)

for x in [1, 2, 3, 4]: 
    print(x)



# while loop 
command = ""
while command.lower() != "quit":      # covert to lowercase then compare
    command = input(">")
    print("echo", command)
