import pickle

from typing import List
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(
    group_list: List[Group],
    file_name: str = "groups.pickle",
) -> int:
    if not group_list:
        return 0
    with open(file_name, "wb") as f:
        pickle.dump(group_list, f)
    max_count_of_students = max(len(group.students) for group in group_list)
    return max_count_of_students


def write_students_information(
    student_list: List[Student],
    file_name: str = "students.pickle",
) -> int:
    with open(file_name, "wb") as f:
        pickle.dump(student_list, f)
    number_of_students = len(student_list)
    return number_of_students


def read_groups_information(
    file_name: str = "groups.pickle"
) -> set:
    try:
        with open(file_name, "rb") as f:
            groups_data = pickle.load(f)
        return {group.specialty.name for group in groups_data}
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return set()


def read_students_information(
    file_name: str = "students.pickle"
) -> List[Student]:
    try:
        with open(file_name, "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []
