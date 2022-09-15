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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty:Specialty
    course: int
    students: List[Student]


def write_groups_information(people: List[Group]):
    with open("groups.pickle", "wb") as file:
        pickle.dump(people, file)
    return max([len(group.students)
                for group in people]) if len(people) > 0 else 0


def write_students_information(people: List[Student]):
    with open("students.pickle", "wb") as file:
        pickle.dump(people, file)
    return len(people)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        people = pickle.load(file)
    return set([group.specialty.name for group in people])


def read_students_information():
    with open("students.pickle", "rb") as file:
        people = pickle.load(file)
    return people
