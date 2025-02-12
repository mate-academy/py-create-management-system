from dataclasses import dataclass
from datetime import datetime
import pickle


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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_num = 0
    with open("groups.pickle", "wb") as group_file:
        pickle.dump(groups, group_file)
        for item in groups:
            if len(item.students) > max_num:
                max_num = len(item.students)
    return max_num


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as read_group:
        result = set()
        current_file = pickle.load(read_group)
        for group in current_file:
            result.add(group.specialty.name)
    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_student:
        current_file = pickle.load(read_student)
    return current_file
