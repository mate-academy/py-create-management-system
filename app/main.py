import dataclasses
import pickle

from datetime import date


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
    students_in_group = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            students_in_group.append(len(group.students))
            pickle.dump(group, file)
    if students_in_group:
        return max(students_in_group)
    return []


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[Specialty]:
    groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break
    return [student for student in students]
