from dataclasses import dataclass
import pickle
from datetime import datetime


@dataclass
class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


@dataclass
class Student:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date: datetime,
            average_mark: float,
            has_scholarship: bool,
            phone_number: str,
            address: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address


@dataclass
class Group:
    def __init__(self, specialty: Specialty, course: int, students: list[Student]) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


def write_groups_information(list_of_group: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_group, f)

    return max((len(students.students) for students in list_of_group), default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)

    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        list_of_students = pickle.load(f)

    return list_of_students
