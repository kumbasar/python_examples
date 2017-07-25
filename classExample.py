students =[]

class Student:

    school_name = "Grundschule"

    def __init__(self,name,student_id=12):
        """
        :param name: 
        :param student_id:
        """
        self.name = name
        self.student_id = student_id
        students.append(self)
        #student ={"name":name, "student_id":student_id}
        #students.append(student)
#    def add_student(self,name,student_id=12):
#        student ={"name":name, "student_id":student_id}
#        students.append(student)
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

jessica = Student("Jessica",11)
print(jessica)

print(Student.school_name)