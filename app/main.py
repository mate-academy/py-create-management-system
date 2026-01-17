import dataclasses
from datetime import datetime
import pickle


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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        if not groups:
            return 0
        result = []
        for group in groups:
            result.append(group)
            pickle.dump(result, f)
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
    return len(students)


def read_groups_information() -> list:
    name_specialty = {}
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                groups = pickle.load(f)
                name_specialty = {group.specialty.name for group in groups}
            except EOFError:
                break
    return sorted(list(name_specialty))


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return students
