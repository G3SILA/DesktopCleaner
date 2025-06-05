# string as array

course = "python let's go"
print(len(course))
print(course[0])
print(course[2 : 4])       # 4 not includedm [2,4)
print(course[:5])
print(course[-1])          # legal in python, o 

first = "hello"
last = "world"
full = first + " " + last
full2 = f"{first} {last}"  #format function 

#same 
print (full)
print (full2)

any_thing_in_between = f"{first} {len(last)} {2 + 2}"

#string as method

print(course.upper())      # uppercase, doesn't mutate original

# lower, title, strip, etc

print(course.replace("p", "1"))    # doesn't mutate either

print ("py" in course)             # True
print (course.find("go"))          # 13   - index
