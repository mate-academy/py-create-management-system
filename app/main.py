import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


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
    students: List[Student]

    @property
    def students_count(self) -> int:
        return len(self.students)


def write_groups_information(groups: list[Group]) -> int:
    file_name = "groups.pickle"

    try:
        with open(file_name, "wb") as file:
            pickle.dump(groups, file)
    except Exception as error:
        print(error)

    if not groups:
        return 0

    max_students = max(group.students_count for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    file_name = "students.pickle"
    students_count = len(students)

    try:
        with open(file_name, "wb") as file:
            pickle.dump(students, file)
    except Exception as error:
        print(error)

    return students_count

def read_groups_information() -> set[str]:
    file_name = "groups.pickle"
    unique_speciality_names = set()

    try:
        with open(file_name, "rb") as file:
            groups = pickle.load(file)
        for group in groups:
            unique_speciality_names.add(group.specialty.name)
    except Exception as error:
        print(error)

    return unique_speciality_names

def read_students_information() -> list[Student]:
    file_name = "students.pickle"
    students_list = []
    try:
        with open(file_name, "rb") as file:
            students = pickle.load(file)
        for student in students:
            students_list.append(student)
    except Exception as error:
        print(error)

    return students_list