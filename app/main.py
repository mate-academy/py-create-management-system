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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:

    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
    try:
        max_value = max(len(group.students) for group in groups)
    except ValueError:
        return
    return max_value


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information() -> list:
    groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break

    specialties = set(group.specialty.name for group in groups)

    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
