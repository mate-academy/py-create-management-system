import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    course: int
    students: [Student]


def write_groups_information(groups: [Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)
    students_groups_len = [len(group.students) for group in groups]
    return max(students_groups_len) if students_groups_len else 0


def write_students_information(students: [Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_groups_information() -> set:
    groups = set()
    with open("groups.pickle", "rb") as groups_file:
        while True:
            try:

                groups.add(pickle.load(groups_file).specialty.name)
            except EOFError:
                break

    return groups


def read_students_information() -> list:
    students = list()
    with open("students.pickle", "rb") as students_file:
        while True:
            try:
                students.append(pickle.load(students_file))
            except EOFError:
                break
    return students
