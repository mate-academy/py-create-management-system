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


def write_groups_information(group: list[Group]) -> int or []:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group, f)
        if group == []:
            return group
        return max([len(i.students) for i in group])


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(student, f)
    return len(student)


def read_groups_information() -> list:
    res = []
    with open("groups.pickle", "rb") as f:
        fl = pickle.load(f)
        for i in fl:
            if i.specialty.name not in res:
                res.append(i.specialty.name)
    return res


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
