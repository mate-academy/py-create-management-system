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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as dump_in:
        pickle.dump(groups, dump_in)
    if groups:
        return max(len(group.students) for group in groups)
    return 0


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", 'wb') as dump_in:
        pickle.dump(students, dump_in)
    return len(students)


def read_groups_information():
    specialty = []

    with open("groups.pickle", "rb") as dump_out:
        data = pickle.load(dump_out)

    for group in data:
        if group.specialty.name not in specialty:
            specialty.append(group.specialty.name)

    return specialty


def read_students_information():
    with open("students.pickle", "rb") as dump_out:
        data = pickle.load(dump_out)

    return data
