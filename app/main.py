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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(ls: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(ls, f)
        if ls:
            return max(len(group.students) for group in ls)
        return 0


def write_students_information(ls: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(ls, f)
        return len(ls)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        result = []
        for group in groups:
            if group.specialty.name not in result:
                result.append(group.specialty.name)
        return result


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        res = []
        for student in students:
            res.append(student)
        return res
