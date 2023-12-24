import dataclasses as dc
import pickle
from datetime import datetime


@dc.dataclass
class Specialty:
    name: str
    number: int


@dc.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dc.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]

    def __gt__(self, other: "Group") -> bool:
        return len(self.students) > len(other.students)


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        max_students_in_group = 0
        for group in groups:
            if len(group.students) > max_students_in_group:
                max_students_in_group = len(group.students)
        return max_students_in_group


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        return (set([group.specialty.name for group in groups])
                if len(groups) else [])


def read_students_information() -> set:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        return students if len(students) else []
