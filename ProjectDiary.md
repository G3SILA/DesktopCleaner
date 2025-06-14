# Start / preparation 
## May 27, 2025
### checklist
- [x] download git desktop    
- [x] learning markdown (progressing!)  
- [ ] decide the specifics of project (or what to do??)  
- [ ] Maybe learning **PYTHON**!!  (script automation I see)

### source 
***Markdown Guide for today***
[markdown guide](https://markdown.com.cn/basic-syntax/emphasis.html 
"you'll see me when your mouse float here - i Know it's cool")

### yes I just learned headlines
> adding an arrow makes the sentence seem wisdom
> because it looks fancy!   
> - and some bulletpoint 
> - 2

and another dash line to separate 

*** 

I think using `code` can be fun. 

I just wonder what can I write for some words.
And what if I don't end with whitespace??



## May 31, 2025
- [ ] start learning python 
- [x] outline of my project - what could it do? 

### source of the day
[python tutorial](https://www.youtube.com/watch?v=K5KVEU3aaeQ "learning in 2 hrs")

### brainstorm 
- clean files on desktop (once per run)
    - by file type and create folder
        - .jpg / .png
        - .docx
        - .pptx
        - .pdf
        - .zip
        - other


    - name folder for designated file type: create if DNE
    - by file name?
        - IMG_
        - Screenshot
        - ...

- automatic clean up from downloading (running at the backend)

- safety / Control
    - Dry-run: Show what would be moved/deleted without actually doing it
    - undo 
    - summary report: xxx files are moved into ... 

- GUI
    - clean
        - preview
    - setting
        - custom file names / target file
    - history
        - recent 5? 



## Jun 1, 2025
- [x] start Python tutorial

### Notes for today
- interpreter 
    - terminal 
    - python hello.py

- extensions
    - lints (help find errors)

- PEP (python enhancement proposal)
    - how python evolve
    - pep 8 (style guide)

- different python implementation
    - Cpython   -> python bytecode
    - Jython (can import `Java code` into python!)  -> java bytecode
    - pypy 


## Jun 4, 2025
- [x] continue on Python   

> This language actually smoothens my brain. I could not differentiate types nor appropritely 
> thinking about managing memory anymore.    

### Notes for today
- string as array 
- string as object 
- math as object! 
- I/O


## Jun 10, 2025
- [x] continue on Python (finish!) 

### Notes for today
**Indentation** matters in Python! 
- if, elif and else
- and, or, not
- MORE smart things that cannot do in other languages

```python
if temperature > 35: 
    print("hot")         # with indentation, inside if 
elif temperature > 20: 
    print("mild")
else: 
    print("cold")
print("done")           #if ends

# in one line
age = 12 
message = "yes" if age >= 18 else "no"
print(message)

if temperature > 0 and age > 12: 
    print("go out and have fun")
elif temperature > 20 or age > 10:
    print("just want to show and, or, not")

# This is legal in python
if 18 <= age < 65:
    print("equivalent to age >= 18 and age < 65")

```

- loop 

```python
# for loop
for number in range(3):   # start from 0 to 2 
    print(number, (number + 1) * "*")
    
# 0 *
# 1 **
# 2 ***
# , works for a space 

for i in range(1, 10, 2):
    print(i) # 1 3 5 7 9 
```


**something new!**
- for else loop: else is only executed if for loop finish without interuption 

Then we have 
- iterables: range, string, list, etc
```python
for i in "python":      # string is an iterable
    print(i)

for x in [1, 2, 3, 4]: 
    print(x)



# while loop 
command = ""
while command.lower() != "quit":      # covert to lowercase then compare
    command = input(">")
    print("echo", command)
```



- list and functions 
```python 
def createlist(*numbers):
    print(numbers)

createlist(1,2,3,4)        #(1, 2, 3, 4)
```


## Jun 14, 2025
- [x] learning python modules 
- [x] start implementing    
    goal for today: 
    - divide files into different folders

**Modules** 
- os
- pathlib

FUN! 
First version of DesktopCleaner.exe released! 
Enter the intend path and clean the files for you! 

