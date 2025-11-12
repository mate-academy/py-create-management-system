import dataclasses
from datetime import date
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
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    if not groups:  # якщо список порожній
        return 0
    return max([len(group.students) for group in groups])


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> set:
    group_list = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                group_list.append(group)
            except EOFError:
                break
    return set([group.specialty.name for group in group_list])


def read_students_information() -> List[Student]:
    student_list = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                student = pickle.load(file)
                student_list.append(student)
            except EOFError:
                break
    return student_list
