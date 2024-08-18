import pickle
from dataclasses import dataclass
from datetime import datetime


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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> set:
    groups_specialities = set()
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    read_groups = pickle.load(file)
                    for group in read_groups:
                        groups_specialities.add(group.specialty.name)
                except EOFError:
                    break
    except FileExistsError:
        print("File 'groups.pickle' not found.")

    return groups_specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_students = pickle.load(file)
    return list_students
