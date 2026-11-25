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
    phone_number: str | int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    max_number_of_students = 0
    for group in group_list:
        if len(group.students) > max_number_of_students:
            max_number_of_students = len(group.students)
    return max_number_of_students


def write_students_information(student_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student_list, f)
    return len(student_list)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as f:
        names = []
        groups = pickle.load(f)
        for group in groups:
            if group.specialty is not None:
                name = group.specialty.name
                if name not in names:
                    names.append(name)
        return names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
