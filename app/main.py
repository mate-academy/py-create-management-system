import dataclasses
import pickle
from datetime import datetime


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
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_file:
        for group in group_list:
            pickle.dump(group, group_file)
    student_amount = [len(group.students) for group in group_list]
    if len(student_amount) > 0:
        return max(student_amount)
    else:
        return []


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in students_list:
            pickle.dump(student, student_file)
    return len(students_list)


def read_groups_information() -> set:
    specialities = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialities.extend([group.specialty.name])
            except Exception:
                return set(specialities)


def read_students_information() -> set:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.extend([student])
            except Exception:
                return students
