from __future__ import annotations
import uuid

class school_class:
    """
    A school class for storing students and prof fields.   
    """
    def __init__(self, name: str, pr: prof):
        self.name = name
        self.prof = pr
        self.list_of_students = []
        self.id = str(uuid.uuid4())
        
    def __str__(self):
        return f"Class {self.name} of faculty {self.faculty_number} \
            with prof {self.prof} has {len(self.list_of_students)} students in it."
    
    def add_student_to_class(self, st: student):
        self.list_of_students.append(st)
        

class faculty:
    def __init__(self, number):
        self.number = number
        self.list_of_classes = []

    def __str__(self):
        return f"Faculty {self.number} "
    
    def add_class_to_faculty(self, Class: school_class):
        self.list_of_classes.append(Class)
    
    @property
    def number_of_students(self):
        return sum([len(_cls.list_of_students) for _cls in self.list_of_classes])
    @property
    def number_of_profs(self):
        return len(self.list_of_classes)
    
class human:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if bool(name):
            self.__name = name
            print("Name has been set")
        else:
            raise ValueError("Name should not be an empty string.")
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age > 0:
            self.age = age
        else:
            raise ValueError("Age must be greater than 0")
    
    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, email):
        if isinstance(email, str) and email.endswith('@gmail.com'):
            self.email = email
        else:
            raise ValueError("We do not accept people who do not have gmail!")
            
        
# st num: st + 2digits for entrance year + 2digits for faculty + 2digits for id
# pr num: pr + 2digits for entrance year + 2digits for faculty + 2digits for id
        
class student(human):
    def __init__(self, name, age, email, avg, faculty_numbr, entrance_year):
        super().__init__(name, age, email)
        self.avg = avg
        self.faculty_number = faculty_numbr
        self.number = 'st' + self.generate_st_number(entrance_year,)
        
    def __str__(self):
        return f"{self.name} with email {self.email} has {self.number}\
            and average score of {self.age}"
    
    def generate_st_number(self):
            pass
    
class prof(human):
    def __init__(self, name, age, email, degree, entrance_year, faculty_number, id):
        super().__init__(name, age, email)
        self.degree = degree
        self.number = self.generate_pr_number(entrance_year, faculty_number, id)
  
    def generate_pr_number(self, entrance_year, faculty_number, id):
        return f"pr{entrance_year}{faculty_number}{id}"
  
  
# Here we go      
faculties = {
    'mechanic': 20,
    'computer': 51,
    'industrial-science': 66,
}
university_faculties_list = []
for f in faculties.keys():
    new_faculty = faculty(faculties[f])
    university_faculties_list.append(new_faculty)


entrance_year_of_each_prof = {
    'bu-azar': (40, 'b@gmail.com', 'PHD', 99),
    'jamali': (40, 'b@gmail.com', 'PHD', 98),
    'karimi': (40, 'b@gmail.com', 'PHD', 01),
    'akbari': (40, 'b@gmail.com', 'PHD', 85),
    'rad': (40, 'b@gmail.com', 'PHD', 90),
    'rahmani': (40, 'b@gmail.com', 'PHD', 00)    
}   


for _faculty in university_faculties_list:
    # Create _faculty's professors
    list_of_profs = []
    for i in range(2):
        new_prof = prof('PHD', _faculty.number, )
        list_of_profs.append(new_prof)
        
    for i in range(1,5):
        new_class = school_class(name=f'andishe{i}', prof='bu-azar')
        _faculty.list_of_classes.append(new_class)