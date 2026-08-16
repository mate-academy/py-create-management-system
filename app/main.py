import dataclasses
import pickle


@dataclasses.dataclass
class Specialty():
    name: str
    number: int


@dataclasses.dataclass
class Student():
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group():
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as outfile:
        pickle.dump(groups, outfile)
        len_groups = 0
        for group in groups:
            if len(group.students) > len_groups:
                len_groups = len(group.students)
    return len_groups


def write_students_information(student: list[Student]) -> int:
    with open("students.pickle", "wb") as outfile:
        pickle.dump(student, outfile)
    return len(student)


def read_groups_information() -> list:
    groups_spec = []
    with open("groups.pickle", "rb") as infile:
        groups = pickle.load(infile)
        for group in groups:
            name = group.specialty.name
            if name not in groups_spec:
                groups_spec.append(name)
    return groups_spec


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as infile:
        students = pickle.load(infile)
    return students
