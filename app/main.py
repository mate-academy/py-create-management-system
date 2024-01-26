from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int

    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: datetime,
        average_mark: float,
        has_scholarship: bool,
        phone_number: str,
        address: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address


@dataclass
class Group:
    specialty: str
    course: int
    students: list[Student]

    def __init__(
        self,
        specialty: str,
        course: int,
        students: list[Student]
    ) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        return max(len(group.students) for group in groups)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
