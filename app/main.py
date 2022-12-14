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


def write_groups_information(group_list: List[Group]) -> int:
    max_students = 0
    for students_size in group_list:
        if len(students_size.students) > max_students:
            max_students = len(students_size.students)
    with open("groups.pickle", "wb") as pickle_group:
        pickle.dump(group_list, pickle_group)
    return max_students


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as pickle_student:
        pickle.dump(student_list, pickle_student)
    return len(student_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as groups_data:
        groups = [
            group.specialty.name
            for group in pickle.load(groups_data)
        ]
    return list(set(groups))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as pickle_students:
        students = pickle.load(pickle_students)
    return students
