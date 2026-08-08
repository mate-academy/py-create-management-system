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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_number_of_students = 0
    with open("groups.pickle", "wb") as file_out:
        for group in groups:
            if len(group.students) > max_number_of_students:
                max_number_of_students = len(group.students)
            pickle.dump(group, file_out)

    return max_number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        for student in students:
            pickle.dump(student, file_out)

    return len(students)


def read_groups_information() -> set:
    groups_specialities = set()
    with open("groups.pickle", "rb") as file_in:
        while True:
            try:
                group = pickle.load(file_in)
                groups_specialities.add(group.specialty.name)
            except EOFError:
                break

    return groups_specialities


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file_in:
        while True:
            try:
                student = pickle.load(file_in)
                students.append(student)
            except EOFError:
                break

    return students
