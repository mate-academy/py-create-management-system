import dataclasses
from datetime import datetime
import pickle
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


def write_groups_information(group_info: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_groups:
        for group in group_info:
            pickle.dump(group, file_groups)

    result = 0
    for group in group_info:
        if len(group.students) > result:
            result = len(group.students)

    return result


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        for student in students_list:
            pickle.dump(student, file_students)

    return len(students_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file_group:
        groups_list = []
        while True:
            try:
                groups_list.append(pickle.load(file_group))
            except EOFError:
                break

    return set([group.specialty.name for group in groups_list])


def read_students_information() -> List[Student]:
    student_list = []

    with open("students.pickle", "rb") as file_students:
        while True:
            try:
                student_list.append(pickle.load(file_students))
            except EOFError:
                break

        return student_list
