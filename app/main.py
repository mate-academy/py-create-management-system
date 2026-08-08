from dataclasses import dataclass
import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list = Student


def write_groups_information(group: Group) -> int:
    with open("groups.pickle", "wb") as gi:
        pickle.dump(group, gi)
    for _ in group:
        return len(_.students)


def write_students_information(student: Student) -> int:
    with open("students.pickle", "wb") as si:
        pickle.dump(student, si)
    return len(student)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pg:
        specialities_of_groups = pickle.load(pg)
    specialities = []
    for i in specialities_of_groups:
        if i.specialty.name not in specialities:
            specialities.append(i.specialty.name)
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as ps:
        students = pickle.load(ps)
    student = []
    for i in students:
        student.append(i)
    return student
