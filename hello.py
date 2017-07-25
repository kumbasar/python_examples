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
except KeyError as error:
    print("Error finding blabla")
    print(error)
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
    print("Error finding last_name")

print("This code executes!")

##############################################

print(set([3,2,3,1,5]))

##############################################

#username = input("Enter username:")
#print(username)

##############################################
students = []
def add_student(name,student_id=123):
    student = {"name": name, "student_id": student_id }
    students.append(student)
    print(students)

add_student("Bo",1)
add_student("Zo")

##############################################

def var_args(name, *args):
    print(name)
    print(args)

var_args("volkan",2,None,False,"bla bla")

##############################################

def var_kargs(name, **kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"],kwargs["subscriber"])

var_kargs("volkan",description="bla bla",feedback=None,subscriber=True)

##############################################

def save_file(value):
    try:
        f = open("test.txt","a")
        f.write(value + "\n")
        f.close()
    except Exception as error:
        print("Could not save file.")
        print(error)

def read_file():
    try:
        f = open("test.txt","r")
        for value in f.readlines():
            print(value)
        f.close()
    except Exception as error:
        print("Could not read file", error)

save_file("test")
save_file("volkan")

read_file()

#######################################################

def read_values():
    try:
        f=open("test.txt","r")
        for student in read_value(f):
            print("->",student)
        f.close()
    except Exception:
        print("Could not read file")

def read_value(f):
    for line in f:
        yield line


read_values()

######################################################

double = lambda x: x * 2

print(double(2))

######################################################
