import dataclasses
from datetime import datetime
import pickle
from typing import Any, List


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
    phone_number: Any
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: Any
    students: List[Student]


def write_groups_information(data: List[Group]) -> int:
    try:
        with open("groups.pickle", "wb") as groups_write:
            pickle.dump(data, groups_write)
        return max(len(instance.students) for instance in data)
    except ValueError:
        return 0


def write_students_information(data: List[Student]) -> int:
    with open("students.pickle", "wb") as students_write:
        pickle.dump(data, students_write)
    return len(data)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as read_group:
        context = pickle.load(read_group)
        result = set()
        for group in context:
            result.add(group.specialty.name)
        return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_students:
        return pickle.load(read_students)
