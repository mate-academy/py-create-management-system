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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(group_list, group_file)
    count_student = 0
    for group in group_list:
        if len(group.students) > count_student:
            count_student = len(group.students)
    return count_student


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students_list, students_file)
    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as group_file:
        groups = pickle.load(group_file)
        name_specialty_list = []
        for group in groups:
            name_specialty_list.append(group.specialty.name)
    return set(name_specialty_list)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as student_file:
        return pickle.load(student_file)
