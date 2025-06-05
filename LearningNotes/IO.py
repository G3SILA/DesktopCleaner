x = input("x: ")
print(x)

# y = x + 1      # type err - x is string not int

print(type(x))   # <class 'str'>
x = int(x)
print(type(x))   # <class 'int'>
y = x + 1
print(y)

print(f"x: {x}, and y: {y}")
