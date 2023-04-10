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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]

    def get_num_students(self) -> int:
        return len(self.students)


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    if group_list:
        return max(group.get_num_students() for group in group_list)


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student_list, f)

    return len(student_list)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        specialties = set()
        for group in groups:
            specialties.add(group.specialty.name)
        return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        students_list = []
        for student in students:
            students_list.append(student)
        return students_list
