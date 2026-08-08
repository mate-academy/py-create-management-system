from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(group: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group, f)
        for student in group:
            if student.students:
                return max(len(student.students) for student in group)
            return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        data_group = pickle.load(f)
        return set(name.specialty.name for name in data_group)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)
        return data
