# write your code here
from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int

    def __hash__(self) -> int:
        return id(self)


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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_group_quantity = 0
    with open("groups.pickle", "wb") as target_file:
        for group in groups:
            pickle.dump(group, target_file)
            max_group_quantity = max(max_group_quantity, len(group.students))
    return max_group_quantity


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as target_file:
        for student in students:
            pickle.dump(student, target_file)
    return len(students)


def read_groups_information() -> list[Group]:
    groups = []
    with open("groups.pickle", "rb") as target_file:
        while True:
            try:
                group = pickle.load(target_file)
            except EOFError:
                break
            else:
                groups.append(group)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as target_file:
        while True:
            try:
                group = pickle.load(target_file)
            except EOFError:
                break
            else:
                students.append(group)
    return students
