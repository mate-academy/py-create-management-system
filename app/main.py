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
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        max_students = 0
        for group in groups:
            pickle.dump(group, pickle_file)
            max_students = max(max_students, len(group.students))
        return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
        return len(students)


def read_groups_information() -> list:
    specialty_names = set()
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                specialty_names.add(group.specialty.name)
            except EOFError:
                break
    return list(specialty_names)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students.append(student)
            except EOFError:
                break
    return students
