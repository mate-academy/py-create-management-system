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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    student_counter = 0

    for group in groups:
        if student_counter < len(group.students):
            student_counter = len(group.students)

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return student_counter


def write_students_information(students: list[Student]) -> int:

    with open("students.pickle", "wb") as file:

        pickle.dump(students, file)

    if len(students) == 0:

        return 0

    return len(students)


def read_groups_information() -> list[Specialty]:

    with open("groups.pickle", "rb") as file:

        groups = pickle.load(file)

        specialties_names = set(group.specialty.name for group in groups)

        return list(specialties_names)


def read_students_information() -> list:

    with open("students.pickle", "rb") as file:

        students = pickle.load(file)

    return students
