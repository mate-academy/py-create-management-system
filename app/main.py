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
    specialty: "Specialty"
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file1:
        pickle.dump(students, file1)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups_list = pickle.load(f)
    specialty_list = []
    for group in groups_list:
        if group.specialty.name not in specialty_list:
            specialty_list.append(group.specialty.name)
    return specialty_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as f1:
        students_list = pickle.load(f1)

    students_output_list = []
    for student_info in students_list:
        students_output_list.append(student_info)
    return students_output_list
