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
    course : int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        for group_obj in groups:
            pickle.dump(group_obj, f)
    if groups:
        max_students = max(len(g.students) for g in groups)
    else:
        max_students = 0
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student_obj in students:
            pickle.dump(student_obj, f)
    return len(students)


def read_groups_information() -> list[str]:
    names = set()
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                group_obj = pickle.load(f)
            except EOFError:
                break
            names.add(group_obj.specialty.name)
    return list(names)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student_obj = pickle.load(f)
            except EOFError:
                break
            students.append(student_obj)
        return students
