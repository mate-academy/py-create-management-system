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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_of_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_group, file)
        if not list_of_group:
            return 0
        return max(len(group.students) for group in list_of_group)


def write_students_information(list_of_students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)
        return len(list_of_students)


def read_groups_information() -> List:
    with open("groups.pickle", "rb") as file:
        group_info = pickle.load(file)
        specialties = {group.specialty.name for group in group_info}
    return list(specialties)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
