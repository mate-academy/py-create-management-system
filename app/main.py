import dataclasses
from datetime import date
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    total_students = len(students)
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return total_students


def read_groups_information() -> list[Group]:
    groups = []
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    group = pickle.load(file)
                    if group.specialty.name not in groups:
                        groups.append(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return groups


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    student = pickle.load(file)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return students
