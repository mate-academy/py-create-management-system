import pickle
import dataclasses
from datetime import datetime


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
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)
    students = []
    for group in groups:
        for student in group.students:
            if student not in students:
                students.append(student)
    return len(students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)
        specialties = []
        for group in groups:
            if group.specialty.name not in specialties:
                specialties.append(group.specialty.name)
        return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
