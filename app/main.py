import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    students_in_groups = []
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            students_in_groups.append(len(group.students))

    return max(students_in_groups, default=0)


def write_students_information(students: Student) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information(groups_file: str = "groups.pickle") -> list[str]:
    groups_specialty = []

    with open(groups_file, "rb") as f:
        while True:
            try:
                group: Group = pickle.load(f)
                groups_specialty.append(group.specialty.name)
            except EOFError:
                break

    return list(set(groups_specialty))


def read_students_information(
        students_file: str = "students.pickle"
) -> list[str]:
    students = []

    with open(students_file, "rb") as f:
        while True:
            try:
                student: Student = pickle.load(f)
                students.append(student)
            except EOFError:
                break

    return students
