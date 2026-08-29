from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(students: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(students, file)
    max_student = 0
    for i in range(len(students)):
        if len(students[i].students) > max_student:
            max_student = len(students[i].students)
    return max_student


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_students, file)
    return len(list_students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        read_file = pickle.load(file)
    result = []
    for name in read_file:
        if name.specialty.name not in result:
            result.append(name.specialty.name)
    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        read_file = pickle.load(file)
    return read_file
