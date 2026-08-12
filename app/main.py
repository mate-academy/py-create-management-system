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
    students: list[Student] = dataclasses.field(
        default_factory=list
    )


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    return (
        max(len(group.students) for group in groups)
        if groups
        else 0
    )


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    loaded_groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                loaded_groups.append(
                    pickle.load(file)
                )
            except EOFError:
                break
    return sorted(
        set(
            group.specialty.name
            for group in loaded_groups
        )
    )


def read_students_information() -> list[Student]:
    loaded_students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                loaded_students.append(
                    pickle.load(file)
                )
            except EOFError:
                break
    return loaded_students
