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
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(groups, groups_file)
    max_student = 0
    for group in groups:
        if len(group.students) > max_student:
            max_student = len(group.students)
    return max_student


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> set:
    groups = []
    with open("groups.pickle", "rb") as groups_file:
        groups.append(pickle.load(groups_file))
    return set(group.specialty.name for group in groups[0])


def read_students_information() -> list:
    with open("students.pickle", "rb") as groups_file:
        students = pickle.load(groups_file)
    return students
