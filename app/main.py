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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(all_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(all_groups, f)
    how_much_students = [len(group.students) for group in all_groups]
    return max(how_much_students, default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        all_groups = pickle.load(f)
    return list(set([group.specialty.name for group in all_groups]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
