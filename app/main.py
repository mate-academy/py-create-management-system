import datetime
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


def write_groups_information(info_group: List[Group]) -> int:
    with open("groups.pickle", "wb") as group:
        pickle.dump(info_group, group)
        max_students = 0
        for student in info_group:
            max_students = max(max_students, len(student.students))
        return max_students


def write_students_information(info_student: List[Student]) -> int:
    with open("students.pickle", "wb") as student:
        pickle.dump(info_student, student)
        return len(info_student)


def read_groups_information() -> List[Specialty]:
    with open("groups.pickle", "rb") as group:
        group_file = pickle.load(group)
        return list(set(group.specialty.name for group in group_file))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as students:
        students_file = pickle.load(students)
        return [student for student in students_file]
