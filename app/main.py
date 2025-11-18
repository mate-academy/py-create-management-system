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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    try:
        return max(len(group.students) for group in groups)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = []
        try:
            while True:
                students.append(pickle.load(file))
        except EOFError:
            pass
    return students
