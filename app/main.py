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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    max_students_num = 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    for unit in groups:
        if Student.first_name in unit.students:
            max_students_num += len(unit.students)

    return max_students_num


def write_students_information(pupil: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(pupil, file)

    return len(pupil)


def read_groups_information() -> set:
    result = []
    with open("groups.pickle", "rb") as file:
        all_groups = pickle.load(file)

    for group in all_groups:
        result.append(group.specialty)

    return set(result)


def read_students_information() -> List:
    with open("students.pickle", "rb") as file:
        all_students = pickle.load(file)

    return all_students
