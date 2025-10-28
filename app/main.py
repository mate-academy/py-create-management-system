import dataclasses
import pickle
from datetime import datetime
from typing import List, Union


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
    course: int  # numer roku
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_obj:
        pickle.dump(groups, file_obj)
    max_students = max(len(group.students)
                       for group in groups) if groups else 0
    return max_students


def write_students_information(
        students_or_groups: List[Union[Student, Group]]) -> int:
    if not students_or_groups:
        all_students = []
    elif isinstance(students_or_groups[0], Group):
        all_students = [student for group in students_or_groups
                        for student in group.students]
    else:
        all_students = students_or_groups

    with open("students.pickle", "wb") as f:
        pickle.dump(all_students, f)

    return len(all_students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file_obj:
        groups = pickle.load(file_obj)

    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_obj:
        students = pickle.load(file_obj)
    return students


def read_max_students() -> int:
    with open("groups.pickle", "rb") as file_obj:
        groups = pickle.load(file_obj)
    max_students = max(len(group.students)
                       for group in groups) if groups else 0
    return max_students


def read_min_students() -> int:
    with open("groups.pickle", "rb") as file_obj:
        groups = pickle.load(file_obj)
    min_students = min(len(group.students)
                       for group in groups) if groups else 0
    return min_students
