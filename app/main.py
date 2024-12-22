import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        groups: list[Group],
        file_path: str = "groups.pickle",
) -> int:
    with open(file_path, "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    max_students_count = 0

    if groups:
        max_students_count = len(
            max(
                groups,
                key=lambda group: len(group.students)
            ).students
        )

    return max_students_count


def write_students_information(
        students: list[Student],
        file_path: str = "students.pickle",
) -> int:
    with open(file_path, "wb") as file:
        for student in students:
            pickle.dump(student, file)

    return len(students)


def read_groups_information(
        file_path: str = "groups.pickle",
) -> set[str]:
    specialities_names = set()

    with open(file_path, "rb") as groups_pickle:
        while True:
            try:
                group = pickle.load(groups_pickle)
                specialities_names.add(group.specialty.name)
            except EOFError:
                break

    return specialities_names


def read_students_information(
        file_path: str = "students.pickle",
) -> list[Student]:
    students = []

    with open(file_path, "rb") as students_pickle:
        while True:
            try:
                student = pickle.load(students_pickle)
                students.append(student)
            except EOFError:
                break

    return students
