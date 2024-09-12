from dataclasses import dataclass
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)
    max_value = len(groups[0].students)
    for i in range(len(groups)):
        if len(groups[i].students) > max_value:
            max_value = len(groups[i].students)
        return max_value


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    data = []
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            data.append(groups)

        specialty_names = set()
        for group in data:
            specialty_names.add(group.specialty.name)
        return list(specialty_names)
    except FileNotFoundError:
        return []


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        return []





