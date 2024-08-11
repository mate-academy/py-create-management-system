# write your code here
import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Speciality:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    speciality: Speciality
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> None:
    with open("groups.pickle", "wb") as handle:
        pickle.dump(groups, handle)

    if not groups:
        return 0

    max_student = max(len(group.students) for group in groups)
    return max_student


def write_students_information(students: list[Student]) -> None:
    with open("students.pickle", "wb") as handle:
        pickle.dump(students, handle)
    return len(students)


def read_groups_information() -> list[Group]:
    with open("groups.pickle", "rb") as handle:
        groups = pickle.load(handle)
    specialities = {group.speciality.name for group in groups}
    return list(specialities)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as handle:
        students = pickle.load(handle)
    return students
