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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max(
        [len(instance.students) for instance in groups]
    ) if groups else []


def write_students_information(instances: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(instances, file)
    return len(instances)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        specialties = set()
        for instance in pickle.load(file):
            specialties.add(instance.specialty.name)
        return specialties


def read_students_information() -> None:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
