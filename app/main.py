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


def write_groups_information(group_members: List[Group]) -> int:
    number = 0
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(group_members, group_file)
        for member in group_members:
            if len(member.students) > number:
                number = len(member.students)
        return number


def write_students_information(students_list: List[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students_list, student_file)
        count = 0
        for _ in students_list:
            count += 1
        return count


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as group_file:
        container = set()
        groups = pickle.load(group_file)
        for group in groups:
            container.add(group.specialty.name)
        return container


def read_students_information() -> list:
    with open("students.pickle", "rb") as student_file:
        students = pickle.load(student_file)
        result = []
        for student in students:
            result.append(student)
        return result
