
"""
таблиці

Адмін
    id
    Ім'я
    Прізвище
        
Викладачі
    id
    Ім'я
    Прізвище
    Що викладає

Батьки
    id
    Ім'я
    Прізвище

Учні
    id
    Ім'я
    Прізвище
    Відповідальний родич

Дисципліни    
    id
    учитель

Успішність
    учень
    дисципліна
    середній бал
    відвідуваність %
"""

from enum import Enum
from hashlib import sha256
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import  declared_attr, MappedColumn, Mapped, Session, DeclarativeBase, relationship

engine = create_engine("sqlite+pysqlite:///model/db1.db", echo=True)

class AbsModel(DeclarativeBase):
    id: Mapped[int] = MappedColumn(autoincrement=True, primary_key=True)
    
    @classmethod
    @declared_attr  
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserType(AbsModel):
    type_name: Mapped[str] = MappedColumn()


class User(AbsModel):
    fullname: Mapped[str] = MappedColumn()
    login: Mapped[str] = MappedColumn()
    password: Mapped[str] = MappedColumn()
    user_type = MappedColumn(ForeignKey("usertype.id"))
    
    
class EducationalSubject(AbsModel):
    subject_name: Mapped[str] = MappedColumn()


class TeacherSubjectModel(AbsModel):
    teacher = MappedColumn(ForeignKey("user.id"))
    educational_subject = MappedColumn(ForeignKey("educationalsubject.id"))


class StudentModel(AbsModel):
    fullname: Mapped[str] = MappedColumn()  
    parents_id = MappedColumn(ForeignKey("user.id"))    


class AcademicPerformance(AbsModel):
    student = MappedColumn(ForeignKey("studentmodel.id"))
    subject = MappedColumn(ForeignKey("educationalsubject.id"))
    subject_grade: Mapped[float] = MappedColumn()
    attendance_rate: Mapped[float] = MappedColumn()



class EUserType(Enum):
    Admin = 1
    Teacher = 2
    Parent = 3



class EEdSubject(Enum):
    Math = 1
    Ukr = 2
    English = 3
    Geog = 4
    Inform = 5
    


def create_tables():
    with Session(engine) as session:
        with session.begin():
            AbsModel.metadata.create_all(engine)
            
     
def mutate_pass(password):
    salt = "0912"
    return sha256(f"{password + salt}".encode("utf-8")).hexdigest()


def login_verify(login: str):
    with Session(engine) as session:
        with session.begin():
            var = session.query(User).filter(User.login == login).first()
            if var is None:
                return 1
            else: 
                return 0


def add_user(fullname: str = '', login: str = '', password: str = '', user_type: int = 0):
    with Session(engine) as session:
        with session.begin():
            user = User(fullname=fullname, login=login, password=mutate_pass(password), user_type=user_type)
            session.add(user)
            
            return session.query(User).filter(User.login == login).first().id # noqa

# add_user("1111", "1111", "1111", EUserType.Admin.value) 

def set_teacher(user_id: int, subject_id: int):
    with Session(engine) as session:
        with session.begin():
            # print(f"Id user = {user_id}")
            teacher = TeacherSubjectModel(teacher=user_id, educational_subject=subject_id)
            session.add(teacher)


def add_student(fullname: str, parent_id: int):
    with Session(engine) as session:
        with session.begin():
            student = StudentModel(fullname=fullname, parents_id=parent_id)
            session.add(student)


def add_academic_performance(student_id: int, subject_id: int, subject_grade: float, attendance_rate: float):
    with Session(engine) as session:
        with session.begin():
            summary = AcademicPerformance(student=student_id, subject=subject_id, subject_grade=subject_grade, attendance_rate=attendance_rate)
            session.add(summary)

def set_academic_performance(id: int, subject_grade: float, attendance_rate: float):
    with Session(engine) as session:
        with session.begin():
            session.query(AcademicPerformance).filter(
                              AcademicPerformance.id == id
                              ).update(
                                  {
                                    AcademicPerformance.subject_grade: subject_grade, 
                                    AcademicPerformance.attendance_rate: attendance_rate
                                   }
                                  )

def get_users_data(type: EUserType, id: int = -1):
    with Session(engine) as session:
        with session.begin():
            if id == -1:
                users = session.query(User).filter(User.user_type == type.value).all()
                return [(user.fullname, user.login, user.id, user.user_type) for user in users]
            else:
                user = session.query(User).filter(User.user_type == type.value, User.id == id).first()
                return [user.fullname, user.login]


def get_students_data(id: int = -1):
    with Session(engine) as session:
        with session.begin():
            if id == -1:
                students = session.query(StudentModel).all()
                return [(std.fullname, std.id, std.parents_id) for std in students]
            else:
                student = session.query(StudentModel).filter(StudentModel.id == id).first()
                if student is None:
                    raise ValueError(f"incorrect student id: {id}")
                return [student.fullname, student.parents_id]


def del_user(id: int):
    with Session(engine) as session:
        with session.begin():
            
            user = session.get(User, id)
            if user.user_type == EUserType.Teacher.value:
                var = session.query(TeacherSubjectModel).filter(TeacherSubjectModel.teacher == user.id).first()
                session.delete(var)
            session.delete(user)


def del_student(id: int):
    with Session(engine) as session:
        with session.begin():
            std = session.get(StudentModel, id)
            session.delete(std)
            

def login(login: str, password: str):
    with Session(engine) as session:
        with session.begin():
            var = session.query(User).filter(User.login == login, User.password == mutate_pass(password)).first()
            if var:
                return {"fullname": f"{var.fullname}", "user_type": f"{var.user_type}", "user_id": f"{var.id}"}
            else:
                return 0


def get_academic_performance(parent_id: int):
    with Session(engine) as session:
        with session.begin():
            std_list = session.query(StudentModel).filter(StudentModel.parents_id == parent_id).all() 
            list_acpf = []
            for std in std_list:
                list_acpf.append(session.query(AcademicPerformance).filter(AcademicPerformance.student == std.id).all())
                   
            return[{"student_id": std.student, 
                    "subject_id": std.subject, 
                    "grade": std.subject_grade, 
                    "attendance_rate": std.attendance_rate, 
                    "id": std.id}  
                   for var in list_acpf for std in var]


def get_academic_performance_tch(subject: EEdSubject):
    with Session(engine) as session:
        with session.begin():
            sub_list = session.query(AcademicPerformance).filter(AcademicPerformance.subject == subject.value).all()
            
            return [(session.get(StudentModel, std.student).fullname, std.student, EEdSubject(std.subject).name, std.subject_grade, std.attendance_rate, std.id) for std in sub_list]


def get_tch_subject(id: int):
    with Session(engine) as session:
        with session.begin():   
            var = session.query(TeacherSubjectModel).filter(TeacherSubjectModel.teacher == id).first()
            return EEdSubject(var.educational_subject)


"""
import json

# logindata
# username user_id login password user_type


data = {
    "logindata": {},
    'admins': {},
    'parents': {},
         
    }
def write_data(path, data):
    with open(f'data.jsonlines', 'a', encoding='utf-8') as file:
        json.dump(data, file)
        file.write('\n')
"""