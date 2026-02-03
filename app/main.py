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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    students: list[Student]
    course: int


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", 'wb') as file:
        pickle.dump(groups, file)
        if not groups:
            return 0
        return max(len(g.students) for g in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", 'wb') as file:
        pickle.dump(students, file)
        return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", 'rb') as file:
        groups = pickle.load(file)
        groups_specialty = []
        for g in groups:
            g = g.specialty.name
            if not g:
                continue
            groups_specialty.append(g)
        groups_specialty = list(set(groups_specialty))
        return groups_specialty


def read_students_information() -> list[Student]:
    with open("students.pickle", 'rb') as file:
        students = pickle.load(file)
        return students
