class person:
    def __init__(self, person_name, person_faculty, person_depart):
        self.person_name = person_name
        self.person_faculty = person_faculty
        self.person_depart = person_depart
        

class student(person):
    def __init__(self, person_name, person_faculty, person_depart, student_id):
        super(person, self).__init__(person_name, person_faculty, person_depart)
        self.student_id = student_id
        
    def study(self):
        print('{}학생이 공부하는 중입니다.'.format(self.person_name))
        

class professor(person):
    def __init__(self, person_name, person_faculty, person_depart, professor_id):
        super(person, self).__init__(person_name, person_faculty, person_depart)
        self.professor_id = professor_id
       

stu1 = student('안가영', '국어국문학과', '국제인문학부', 20180062)
stu2 = student('안나영', '국어국문학과', '국제인문학부', 20180063)
print(stu1.study())
        
        
class department:
    def __init__(self, depart_name, depart_mail, faculties=None):
        self.depart_name = depart_name
        self.depart_mail = depart_mail
        if faculties is None:
            self.faculties = []
        else:
            self.faculties = faculties
            
    def add_faculty(self, new_faculties):
        for n_faculty in new_faculties:
            if n_faculty not in self.faculties:
                self.faculties.append(n_faculty)
            else:
                print('이미 추가된 학과입니다.')
                
    def remove_faculty(self, del_faculties):
        for d_faculty in del_faculties:
            try:
                self.faculties.remove(d_faculty)
            except:
                print('없는 학과입니다.')
    
    
class faculty:
    def __init__(self, faculty_name, faculty_mail, students=None, professors=None):
        self.faculty_name = faculty_name
        self.faculty_mail = faculty_mail
        if students is None:
            self.students = []
        else:
            self.students = students
    
    def add_student(self, new_students):
        for n_student in new_students:
            if n_student not in self.students:
                self.students.append(n_student)
            else:
                print('이미 소속된 학생입니다.')
                
    def remove_student(self, del_students):
        for d_student in del_students:
            try:
                self.students.remove(d_student)
            except:
                print('소속되지 않은 학생입니다.')
                
    def show_students(self):
        list_of_students = [x for x in self.students]
        num_of_students = len(list_of_students)
