import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    names_of_specialties = set()
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    for group in groups:
        names_of_specialties.add(group.specialty.name)
    return list(names_of_specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
