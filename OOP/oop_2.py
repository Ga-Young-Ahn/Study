student = {'name':'이상희', 'year':2, 'class':3, 'student_id': 35}
print('{}, {}학년 {}반 {}번'.format(student['name'], student['year'], student['class'], student['student_id']))

class Student:
    def __init__(self, name, year, class_num, student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id
        
    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)

student = Student('이상희', 2, 3, 35)
print(student.introduce_myself())



import student
print('{}, {}학년 {}반 {}번'.format(student.name, student.year, student.class_id, student.student_id))


text = 'string'
print(dir(text))

print('text의 클래스 확인')
print(text.__class__)
print('text가 str의 인스턴스 오브젝트인지 확인')
print(isinstance(text, str))
print('str 오브젝트의 메소드 확인')
print(text.upper())


def my_function():
    '''my_function에 대한 설명'''
    pass

print('mf의 속성 확인')
print(dir(my_function))
print('mf의 docstring 출력')
print(my_function.__doc__)
print('mf에 새로운 속성 추가')
my_function.new_variable = '새로운 변수입니다'
print('추가된 속성 확인')
print(dir(my_function))
print('추가한 속성값 출력')
print(my_function.new_variable)




class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print('emp_1과 emp_2는 다른 메모리 주소값을 가진 별개의 오브젝트입니다')
print(id(emp_1))
print(id(emp_2))
print()
print('emp_1과 emp_2는 같은 클래스의 인스턴스인 것을 확인합니다')
class_of_emp_1 = emp_1.__class__
class_of_emp_2 = emp_2.__class__
print(id(class_of_emp_1))
print(id(class_of_emp_2))



class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = '가영'
emp_1.last = '안'
emp_1.email = 'abc.gmail.com'
emp_1.pay = 50000

emp_2.first = '가영2'
emp_2.last = '안2'
emp_2.email = 'abc2.gmail.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)



class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('Sanghee', 'Lee', 4000)
emp_2 = Employee('Minjung', 'Kim', 3000)

print(emp_1.full_name())

print(Employee.full_name(emp_1))