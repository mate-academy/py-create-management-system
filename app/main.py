from datetime import date
import pickle
import dataclasses


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    max_students = 0
    for group in groups:
        current_students = len(group.students)
        if current_students > max_students:
            max_students = current_students

    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: list[Student]) -> int:
    number_of_students = len(students)

    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return number_of_students


def read_groups_information() -> list:
    specialty_names = []

    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    for group in groups:
        name = group.specialty.name
        if name not in specialty_names:
            specialty_names.append(name)

    return specialty_names


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
