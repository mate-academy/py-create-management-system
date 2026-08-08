import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: type[datetime]
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
    number_of_students = 0
    with open("groups.pickle", "wb") as file_out:
        for group in groups:
            if number_of_students < len(group.students):
                number_of_students = len(group.students)
            pickle.dump(group, file_out)
    return number_of_students


def write_students_information(students: list[Student]) -> None:
    with open("students.pickle", "wb") as file_out:
        for student in students:
            pickle.dump(student, file_out)
    return len(students)


def read_groups_information() -> list[Group]:
    groups = []
    with open("groups.pickle", "rb") as file_in:
        while True:
            try:
                group = pickle.load(file_in)
                groups.append(group.specialty.name)
            except EOFError:
                break
    return list(set(groups))


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file_in:
        while True:
            try:
                students.append(pickle.load(file_in))
            except EOFError:
                break
    return students
