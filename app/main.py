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
    birth_date: datetime
    average_mark: float
    has_scholarsip: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student] = dataclasses.field(default_factory=list)


def write_group_information(groups: list[Group]) -> int:
    max_studesnts = 0
    with open("groups.pickle", "wb") as file_name:
        for group in groups:
            pickle.dump(group, file_name)
            if len(group.students) > max_studesnts:
                max_studesnts = len(group.students)
    return max_studesnts


def write_student_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_name:
        for student in students:
            pickle.dump(student, file_name)
    return len(students)


def read_groups_information() -> list[str]:
    unique_names = set()
    with open("groups.pickle", "rb") as file_name:
        while True:
            try:
                group = pickle.load(file_name)
            except EOFError:
                break
            unique_names.add(group.specialty.name)
    return list(unique_names)


def read_students_information() -> list[Student]:
    students: list[Student] = []
    with open("students.pickle", "rb") as file_name:
        while True:
            try:
                student = pickle.load(file_name)
            except EOFError:
                break
            students.append(student)
    return students
