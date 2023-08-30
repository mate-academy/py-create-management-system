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
    course: str
    student: Student


def write_groups_information(lyceum_groups: List[Group]) -> int:
    pass


def write_students_information(students: List[Student]) -> int:
    pass


def read_groups_information(file_groups: str) -> List[Group]:
    pass


def read_students_information(file_students: str) -> List[Student]:
    pass
