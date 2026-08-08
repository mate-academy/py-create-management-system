import dataclasses
from datetime import datetime
from typing import List
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    list_students = []
    for student in groups:
        list_students.append(len(student.students))
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max(list_students) if list_students else 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    result = set([])
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    for i in groups:
        result.add(i.specialty.name)
    return list(result)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
