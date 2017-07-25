print("Hello World")

answer = 42
name = "PythonBo"

def add_numbers(a,b):
    print(a + b)

add_numbers(3,4)

pi = 3.14

print(pi)
print(int(pi))

print("hello".capitalize())
print("hello".isalpha())
print("23".isdigit())
print("hello".replace("e","3"))
aa = "some,csv,values".split(",")
print(aa)

name  = "pythonV"
machine = "HAL"

print ("Nice to meet you {0}. I am {1}.".format(name,machine))
print (f"Nice to meet you {name}. I am {machine}.")

python = True
java_course = False

print(python)
print(java_course)

print(int(python))
print(int(java_course))

aliens_found = None

number = 5
if number:
    print("Number is defined and truthy")
else:
    print("Number is NOT 5")

if number == 5:
    print("Number is 5")
if not java_course:
    print("java_course is FALSE")
if number == 5 and not java_course:
    print(" 5 and FALSE")

a = 1
b = 2
print("bigger" if a > b else "smaller")

student_names = ["Mark", "Wolfgang", "Anja"]

print(student_names[1])
print(student_names[2])
print(student_names[-1])
student_names[-1] = "Volkan"
print(student_names)
student_names.append("Grey") #Appent a value
print(student_names)
print("Volkan" in student_names) #
print(len(student_names)) #length of array
del student_names[2] #delete volkan
print(student_names)
print(student_names[1:-1])

student_names = ["Mark", "Wolfgang", "Anja","Tatjana"]

for name in student_names:
    print("Student name {0}".format(name))
    if name == "Anja":
        print("Anja")
        break

for index in range(1,10):
    print(index*10)

x = 0

while x < 10:
    print ("Count is {0}".format(x))
    x+=1

student = {
    "name": "Mark",
    "student_id":12323,
    "feedback": None
}

print (student["name"]);
print (student.get("blabla","unknown"))
print (student.keys())
print (student.values())

#Exception handling
try:
    last_name = student["blabla"]
    print(last_name)
except KeyError:
    print("Error finding blabla")
except TypeError:
    print("Type Error blabla")
except Exception:
    print("Unknown Error")

print("This code executes!")

student["last_name"] = "Wiki"
try:
    last_name = student["last_name"]
    print(last_name)
except KeyError:
    print("Error finding blabla")

print("This code executes!")
