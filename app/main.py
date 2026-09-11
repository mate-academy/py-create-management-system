from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    specialty_names = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    group = pickle.load(file)
                    specialty_names.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return list(specialty_names)


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
