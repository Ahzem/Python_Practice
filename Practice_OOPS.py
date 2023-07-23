class Student:
    def __init__(self):
        self.__name = None
        self.__age = None
        self.__roll_no = None
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_roll_no(self):
        return self.__roll_no
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
        
    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no
        
    def display_details(self):
        print(f"{self.__name} is {self.__age} years old and his roll number is {self.__roll_no}")
        
        
class SchoolStudent(Student):
    def __init__(self):
        super().__init__()
        
class CollegeStudent(Student):
    def __init__(self):
        super().__init__()
        
saman = SchoolStudent()
saman.set_name("Saman")
saman.set_age(15)
saman.set_roll_no(1)
saman.display_details()

aasif = CollegeStudent()
aasif.set_name("Aasif")
aasif.set_age(20)
aasif.set_roll_no(1)
aasif.display_details()