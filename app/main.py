from dataclasses import dataclass
import pickle
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_write_pickle:
        for group in groups:
            pickle.dump(group, groups_write_pickle)
    maximum_students = [len(group.students) for group in groups]
    if maximum_students:
        return max(maximum_students)
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_write_pickle:
        for student in students:
            pickle.dump(student, students_write_pickle)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as groups_read_pickle:
        loaded_groups = []
        while True:
            try:
                loaded_groups.append(pickle.load(groups_read_pickle))
            except EOFError:
                break

        specialty_name = list(set(group.specialty.name
                                  for group in loaded_groups))
    return specialty_name


def read_students_information() -> list:
    with open("students.pickle", "rb") as students_read_pickle:
        loaded_students = []
        while True:
            try:
                loaded_students.append(pickle.load(students_read_pickle))
            except EOFError:
                break
    return loaded_students
