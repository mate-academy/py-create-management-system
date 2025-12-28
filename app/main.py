import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int | None:
    number_of_students = []
    with open("groups.pickle", "wb") as file_pickle:
        for group in groups:
            number_of_students.append(len(group.students))
            pickle.dump(group, file_pickle)
    if number_of_students:
        return max(number_of_students)
    return 0


def write_students_information(students: List[Student]) -> None:
    number_of_students = 0
    with open("students.pickle", "wb") as file_pickle:
        for student in students:
            number_of_students += 1
            pickle.dump(student, file_pickle)
    return number_of_students


def read_groups_information() -> List[Group]:
    groups_specs = []
    try:
        with open("groups.pickle", "rb") as file_pickle:
            while True:
                group = pickle.load(file_pickle)
                groups_specs.append(group.specialty.name)
    except EOFError:
        pass
    unique_specs = list(dict.fromkeys(groups_specs))
    return unique_specs


def read_students_information() -> List[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as file_pickle:
            while True:
                student = pickle.load(file_pickle)
                students.append(student)
    except EOFError:
        pass
    return students
