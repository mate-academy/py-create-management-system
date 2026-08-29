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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    groups_specialties = set()
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    read_groups = pickle.load(f)
                    for group in read_groups:
                        groups_specialties.add(group.specialty.name)
                except EOFError:
                    break
    except FileExistsError:
        print("File 'groups.pickle' does not exist")

    return groups_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        list_students = pickle.load(f)

    return list_students
