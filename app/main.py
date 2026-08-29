from __future__ import annotations

import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str | datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

    def __repr__(self) -> Student:
        return Student(
            first_name=self.first_name,
            last_name=self.last_name,
            birth_date=datetime.strptime(self.birth_date, "%Y-%m-%d"),
            average_mark=self.average_mark,
            has_scholarship=self.has_scholarship,
            phone_number=self.phone_number,
            address=self.address,
        )


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_group = 0
    for group in groups:
        if len(group.students) > max_group:
            max_group = len(group.students)
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    return max_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(students, students_file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return set([group.__dict__.get("specialty").name for group in groups])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return [student for student in students]
