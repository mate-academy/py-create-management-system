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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)

        if not list_of_groups:
            return 0

    max_students = 0
    for group in list_of_groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)

    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

        specialty_names = set()
        for group in groups:
            specialty_names.add(group.specialty.name)

        return specialty_names


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_of_students = pickle.load(file)

    return list_of_students
