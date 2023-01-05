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
    with open("groups.pickle", "wb") as pickle_file:
        count_student = [0]
        for group in groups:
            pickle.dump(group, pickle_file)
            count_student.append(len(group.students))
        return max(count_student)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as pickle_file:
        groups = []
        while True:
            try:
                groups.append(pickle.load(pickle_file))
            except EOFError:
                return list({some.specialty.name for some in groups})


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        students = []
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break
        return students
