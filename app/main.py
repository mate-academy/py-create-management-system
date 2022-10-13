from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set(group.specialty.name for group in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return [student for student in students]
