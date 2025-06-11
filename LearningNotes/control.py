temperature = 25

if temperature > 35:
    print("hot")
elif temperature > 20:
    print("mild")
else:
    print("cold")
print("done")

age = 22
message = "yes" if age >= 18 else "no"
print(message)

if temperature > 0 and age > 12:
    print("go out and have fun")
elif temperature > 20 or age > 10:
    print("just want to show and, or, not")

# This is legal in python
if 18 <= age < 65:
    print("equivalent to age >= 18 and age < 65")

# loop
for number in range(3):   # start from 0 to 2 
    print(number, (number + 1) * "*")
    
# 0 *
# 1 **
# 2 ***
# , works for a space 

for i in range(1, 10, 2):   # start 1， without 10, step by 2
    print(i) # 1 3 5 7 9 
    if (i > 11): 
        break 
else: 
    print("run through")
