import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: int


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list) -> int:
    max_stud = 0
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            if len(group.students) > max_stud:
                max_stud = len(group.students)
    return max_stud


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as f:
        try:
            while True:
                group = pickle.load(f)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return specialties


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as f:
        try:
            while True:
                student = pickle.load(f)
                students.append(student)
        except EOFError:
            pass
    return students[0]
