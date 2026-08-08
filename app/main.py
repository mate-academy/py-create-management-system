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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as group_pickle:
        pickle.dump(group_list, group_pickle)
    group_students_list = []
    for group in group_list:
        group_students_list.append(len(group.students))
    if group_students_list:
        return max(group_students_list)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        pickle.dump(students_list, students_pickle)
        return len(students_list)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as read_group_pickle:
        unique_subjects = []
        group_list = pickle.load(read_group_pickle)
        for group in group_list:
            if group.specialty.name not in unique_subjects:
                unique_subjects.append(group.specialty.name)
        return unique_subjects


def read_students_information() -> None:
    with open("students.pickle", "rb") as read_students_pickle:
        return pickle.load(read_students_pickle)
