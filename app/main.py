import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    students_list = []
    for group in groups:
        students_list.append(len(group.students))
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not students_list:
        return 0
    return max(students_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialties_list = []
        for group in groups:
            specialties_list.append(group.specialty.name)
        return set(specialties_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
