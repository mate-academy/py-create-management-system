import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass
class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


@dataclasses.dataclass
class Student:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: datetime,
                 average_mark: float,
                 has_scholarship: bool,
                 phone_number: str,
                 address: str,
                 ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        max_students = max(
            len(group.students) for group in groups) if groups else 0
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialties = {group.specialty.name for group in groups}
        return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
