import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass()
class Specialty:
    name: str
    number: str


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_to:
        pickle.dump(groups, file_to)
    if groups:
        return max((len(group.students) for group in groups))
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_to:
        pickle.dump(students, file_to)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file_from:
        groups = pickle.load(file_from)
    result = list(set([group.specialty.name for group in groups]))
    print(result)
    return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_from:
        students = pickle.load(file_from)
    return students
