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
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        student_amount = [len(group.students) for group in groups]
        return max(student_amount) if student_amount else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialities = set()
        for group in groups:
            specialities.add(group.specialty.name)
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
