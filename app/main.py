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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course : int
    students : list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = max(len(group.students)
                       for group in groups) if groups else 0

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)

        specialties = set(group.specialty.name for group in groups)
        return sorted(specialties)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
