import dataclasses
from datetime import datetime
import pickle


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
    course : int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int | list:
    with open("groups.pickle", "wb") as group_file:
        for group in group_list:
            pickle.dump(group, group_file)
    students_amount = [len(group.students) for group in group_list]
    if len(students_amount) > 0:
        return max(students_amount)
    else:
        return []


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        for student in student_list:
            pickle.dump(student, student_file)
    return len(student_list)


def read_groups_information() -> set:
    specialties = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialties.extend([group.specialty.name])
            except Exception:
                return set(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.extend([student])
            except Exception:
                return students
