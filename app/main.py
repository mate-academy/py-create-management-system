import dataclasses
import pickle

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
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    return (
        max(len(group.students) for group in groups) if len(groups) else 0
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_read:
        specialties = set()
        try:
            while True:
                group = pickle.load(groups_read)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_read:
        result = []
        try:
            while True:
                student = pickle.load(students_read)
                result.append(student)
        except EOFError:
            pass
    return result
