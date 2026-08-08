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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> Student:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    total_students = len(students)
    return total_students


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return list(students)
