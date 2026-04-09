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


def write_groups_information(list_of_groups: list[Group]) -> int:
    if list_of_groups:
        with open("groups.pickle", "wb") as file:
            for group in list_of_groups:
                pickle.dump(group, file)

    max_students = max((len(group.students)
                        for group in list_of_groups), default=0)

    return max_students


def read_groups_information() -> list[str]:
    groups = []
    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    groups.append(pickle.load(file))
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    name_speciality = []
    for group in groups:
        if group.specialty.name not in name_speciality:
            name_speciality.append(group.specialty.name)

    return name_speciality


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in list_of_students:
            pickle.dump(student, file)

    return len(list_of_students)


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file:
            while True:
                try:
                    students.append(pickle.load(file))
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return students
