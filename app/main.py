import pickle
from dataclasses import dataclass
from typing import List, Any


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> List[Any] | int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        if not groups:
            return []
        return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file_l:
        groups = pickle.load(file_l)
        return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_l:
        return pickle.load(file_l)
