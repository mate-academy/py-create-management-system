import dataclasses
import pickle
from datetime import date
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]):

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    result = [len(group.students) for group in groups]

    return max(result) if len(result) > 0 else []


def write_students_information(students: List[Student]):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information():
    result = []

    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

        for group in groups:
            if group.specialty.name not in result:
                result.append(group.specialty.name)

    return result


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

        return students
