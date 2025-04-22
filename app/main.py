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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        result = max((len(group.students) for group in groups), default=0)
        pickle.dump(groups, file)
    return result


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


def read_groups_information() -> list[Group]:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            for group in groups:
                specialties.add(group.specialty.name)
    except (EOFError, FileNotFoundError):
        return []

    return list(specialties)


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            return pickle.load(file)
    except (EOFError, FileNotFoundError):
        return []
