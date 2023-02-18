from __future__ import annotations
import uuid
import re


class School_Class:
    """
    A school class for storing students and prof fields.   
    """

    def __init__(self, name: str, pr: Prof):
        self.name = name
        self.prof = pr
        self.list_of_students = []
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"Class {self.name} \
            with prof {self.prof} has {len(self.list_of_students)} students in it."

    def add_student_to_class(self, st: Student):
        self.list_of_students.append(st)


class Faculty:
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


class Human:
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
        else:
            raise ValueError("Name should not be an empty string.")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if int(age) > 0:
            self.__age = age
        else:
            raise ValueError("Age must be greater than 0")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, email)):
            self.__email = email
        else:
            raise ValueError("Invalid Email!")


# st num: st + 2digits for entrance year + 2digits for faculty + 2digits for id
# pr num: pr + 2digits for entrance year + 2digits for faculty + 2digits for id

class Student(Human):
    def __init__(self, name, age, email, score, avg, faculty_numbr, entrance_year, id):
        super().__init__(name, age, email)
        self.score = score
        self.avg = avg
        self.faculty_number = faculty_numbr
        self.number = self.generate_st_number(entrance_year, faculty_numbr, id)

    def __str__(self):
        return f"{self.name} with email {self.email} has {self.number}\
            and average score of {self.avg}"

    def generate_st_number(self, entrance_year, faculty_number, id):
        return f"st{entrance_year}{faculty_number}{id}"

    def __add__(self, other):
        return self.score + other.score

    def __gt__(self, other):
        return self.score > other.score


class User(Human):
    def __init__(self, name, phone_number, email, password, address):
        super().__init__(name, email)
        self.phone_number = phone_number
        self.password = password
        self.address = address

    @property
    def password(self):
        return self.__password

    @password.setter
    def set_password(self, password):
        l, u, p, d = 0, 0, 0, 0
        s = "R@m@_f0rtu9e$"
        capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets="abcdefghijklmnopqrstuvwxyz"
        specialchar="$@_"
        digits="0123456789"
        if (len(s) >= 8):
            for i in s:
                if (i in smallalphabets):
                    l+=1           
                if (i in capitalalphabets):
                    u+=1           
                if (i in digits):
                    d+=1           
                if(i in specialchar):
                        p+=1       
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
            self.__password = password
        else:
            print("Invalid Password")


class Staff(User):
    def __init__(self, name, phone_number, email, password, address, service_location_name, service_location_info, salary):
      super().__init__(name, phone_number, email, password, address)
      self.service_location_name = service_location_name
      self.service_location_info = service_location_info
      self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def final_salary(self):
        if self.salary <= 5000000 :
            insurance =int(0.07 * self.salary)
            tax =int(0.09 * self.salary)
            return self.salary - insurance - tax
        else :
            insurance = 0.07 * (self.salary-5000000)
            tax = 0.09 * (self.salary-5000000)
            return self.salary - insurance - tax


class Prof(Staff):
    def __init__(self, name, age, email, degree, entrance_year, faculty_number, id, salary):
        super().__init__(name, age, email, salary)
        self.degree = degree
        self.number = self.generate_pr_number(
            entrance_year, faculty_number, id)

    def __str__(self):
        return f"{self.name} has {self.degree} with {self.salary} salary."

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
    new_faculty = Faculty(faculties[f])
    university_faculties_list.append(new_faculty)


entrance_year_of_each_prof = {
    'bu-azar': ('41', 'b@gmail.com', 'PHD', '99'),
    'jamali': ('42', 'j@gmail.com', 'PHD', '98'),
    'karimi': ('44', 'k@gmail.com', 'PHD', '01'),
    'akbari': ('45', 'a@gmail.com', 'PHD', '85'),
    'rad': ('39', 'r@gmail.com', 'PHD', '90'),
    'rahmani': ('85', 'ra@gmail.com', 'PHD', '00')
}


for _faculty in university_faculties_list:
    # Create _faculty's professors
    list_of_profs = []
    for i in range(1, 3):
        new_item = entrance_year_of_each_prof.popitem()
        new_prof = Prof(new_item[0], *new_item[1],
                        str(_faculty.number), str(i))
        list_of_profs.append(new_prof)

    for i in range(1, 5):
        new_class = School_Class(name=f'andishe{i}', pr=list_of_profs[i % 2])
        for _stu in range(10):
            new_student = Student(name=str(_stu), age=22, email='s@gmail.com',
                                  avg=20, faculty_numbr=_faculty.number, entrance_year=98, id=_stu)
            new_class.add_student_to_class(new_student)
        _faculty.list_of_classes.append(new_class)

for _fac in university_faculties_list:
    print(_fac)
    for _class in _fac.list_of_classes:
        print(_class)
