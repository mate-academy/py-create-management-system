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
    students: list


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0

    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

            if len(group.students) > max_students:
                max_students = len(group.students)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list[str]:
    unique_specialties = set()

    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                unique_specialties.add(group.specialty.name)
            except EOFError:
                break

    return list(unique_specialties)


def read_students_information() -> list[Student]:
    students_list = []

    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                students_list.append(student)
            except EOFError:
                break

    return students_list
