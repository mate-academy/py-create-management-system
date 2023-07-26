from dataclasses import dataclass
from datetime import datetime
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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_amount_of_students = 0
    with open("groups.pickle", "wb") as groups_pickle_file:
        for group in groups:
            pickle.dump(group, groups_pickle_file)
            max_amount_of_students = (
                len(group.students)
                if len(group.students) > max_amount_of_students
                else max_amount_of_students
            )

    return max_amount_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle_file:
        for student in students:
            pickle.dump(student, students_pickle_file)

    return len(students)


def read_groups_information() -> list[Group]:
    specialities = {}
    with open("groups.pickle", "rb") as groups_pickle_file:
        while True:
            try:
                specialities[
                    pickle.load(groups_pickle_file).specialty.name
                ] = ""
            except EOFError:
                break

    return list(specialities)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as students_pickle_file:
        while True:
            try:
                students.append(pickle.load(students_pickle_file))
            except EOFError:
                break

    return students
