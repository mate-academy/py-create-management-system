import dataclasses
from datetime import datetime
import pickle
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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_groups: List[Group]):
    with open("groups.pickle", "wb") as groups_pickle:
        pickle.dump(list_groups, groups_pickle)
    for group in list_groups:
        group_list = [len(group.students)]
        if not len(group_list):
            return []
        return max(group_list)


def write_students_information(list_students: List[Student]):
    with open("students.pickle", "wb") as student_pickle:
        pickle.dump(list_students, student_pickle)
    return len(list_students)


def read_groups_information():
    with open("groups.pickle", "rb") as groups_pickle:
        new_list = [group.specialty.name
                    for group in pickle.load(groups_pickle)]
    return set(new_list)


def read_students_information():
    with open("students.pickle", "rb") as student_pickle:
        new_list = pickle.load(student_pickle)
    return new_list
