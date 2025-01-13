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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    return max_students


def write_students_information(students: list[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return num_students


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
    groups_specialities = {group.specialty.name for group in groups}

    return list(groups_specialities)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        students = pickle.load(pickle_file)

    return students
