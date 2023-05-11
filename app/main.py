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
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    result = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            result.append(len(group.students))

    return max(result) if result else 0


def write_students_information(students: list[Student]) -> int:
    result = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            result += 1

    return result


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as file:
            result = []
            while True:
                try:
                    result.append(pickle.load(file).specialty.name)
                except EOFError:
                    break
            return list(set(result))
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    result = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                result.append(pickle.load(file))
            except EOFError:
                return result
