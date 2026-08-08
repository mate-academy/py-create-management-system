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
    birth_date: datetime.date
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
    with open("groups.pickle", "wb") as pickle_group:
        for group in groups:
            pickle.dump(group, pickle_group)
    students_in_groups = [len(group.students) for group in groups]
    return max(students_in_groups) if students_in_groups != [] else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_students:
        for student in students:
            pickle.dump(student, pickle_students)
    return len(students)


def read_groups_information() -> set[Specialty]:
    groups = []
    with open("groups.pickle", "rb") as pickle_groups:
        try:
            while True:
                group = pickle.load(pickle_groups)
                groups.append(group)
        except EOFError:
            pass

    specialties = [group.specialty for group in groups]
    names_of_specialties = [specialty.name for specialty in specialties]
    return set(names_of_specialties)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_students:
        try:
            while True:
                student = pickle.load(pickle_students)
                students.append(student)
        except EOFError:
            pass
    return students
