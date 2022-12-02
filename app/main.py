import pickle
from dataclasses import dataclass
from typing import List


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: List[Student]


def write_groups_information(student_groups: List[Group]) -> int:
    maximum_students_number_list = []

    for group in student_groups:
        maximum_students_number_list.append(len(group.students))
    with open("groups.pickle", "wb") as f:
        pickle.dump(student_groups, f)

    return max(maximum_students_number_list, default=0)


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> set:
    all_specialities = []
    with open("groups.pickle", "rb") as f:
        groups_data = pickle.load(f)
    for group in groups_data:
        all_specialities.append(group.specialty.name)
    return set(all_specialities)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
