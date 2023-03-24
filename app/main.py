from dataclasses import dataclass
from typing import List
import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_pickle:
        pickle.dump(group, file_pickle)

    if len(group) != 0:
        return max([len(member.students) for member in group])


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_pickle:
        pickle.dump(students, file_pickle)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_pickle:
        group = pickle.load(file_pickle)
    return set(member.specialty.name for member in group)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_pickle:
        students = pickle.load(file_pickle)
    return students
