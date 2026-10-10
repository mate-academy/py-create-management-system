import pickle

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]



def write_groups_information():
    pass

def write_students_information():
    pass


def read_groups_information():
    pass


def read_students_information():
    pass


# birth_date=datetime(2005, 5, 15)
# print(birth_date)
# print(type(birth_date))

