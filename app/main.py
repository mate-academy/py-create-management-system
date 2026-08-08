import dataclasses
import pickle
from datetime import datetime
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
    course: datetime
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:

    if not groups:
        return 0

    max_students = max(len(group.students) for group in groups)

    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    return max_students


def write_students_information(students: List[Student]) -> int:

    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = []
            while True:
                try:
                    group = pickle.load(file)
                    if group.specialty.name not in groups:
                        groups.append(group.specialty.name)
                except EOFError:
                    break
                except FileNotFoundError:
                    groups = []

        return groups
    except FileNotFoundError:
        return []


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
