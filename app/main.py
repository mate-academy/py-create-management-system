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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        if len(groups) != 0:
            return max([len(group.students) for group in groups])
        else:
            return 0


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups_data = pickle.load(f)
        return set([i.specialty.name for i in groups_data])


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_students_information() -> object:
    with open("students.pickle", "rb") as f:
        students_data = pickle.load(f)
        return students_data
