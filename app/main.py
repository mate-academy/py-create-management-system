import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(groups, file_group)
    res = 0
    for student in groups:
        if len(student.students) > res:
            res = len(student.students)
    return res


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(students, file_students)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_group:
        list_group = pickle.load(file_group)
    res = set()
    for lst_gro in list_group:
        res.add(lst_gro.specialty.name)
    return list(res)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file_student:
        list_student = pickle.load(file_student)
    return list_student
