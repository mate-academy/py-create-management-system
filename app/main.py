import dataclasses
from datetime import datetime
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(group_list: List[Group]) -> int:
    with open("groups.pickle", 'wb') as dump_in:
        pickle.dump(group_list, dump_in)

    if group_list:
        return max(len(group.students) for group in group_list)

    return 0


def write_students_information(student_list: List[Student]) -> int:
    with open("students.pickle", 'wb') as dump_in:
        pickle.dump(student_list, dump_in)
    return len(student_list)


def read_groups_information():
    specialty_name = []

    with open("groups.pickle", "rb") as dump_out:
        data = pickle.load(dump_out)

    for group in data:
        if group.specialty.name not in specialty_name:
            specialty_name.append(group.specialty.name)

    return specialty_name


def read_students_information():
    with open("students.pickle", "rb") as dump_out:
        data = pickle.load(dump_out)

    return data
