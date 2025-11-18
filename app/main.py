import dataclasses
import pickle

from datetime import datetime
#from __future__ import annotations


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime  # TODO: Clarify that!
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int  # TODO: Clarify that!
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    pass
