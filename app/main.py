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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as outfile:
        pickle.dump(groups, outfile)
    names = []
    for group in groups:
        names += [student.first_name for student in group.students]
    students = len(set(names))
    return students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as outfile:
        pickle.dump(students, outfile)
    return len(students)


def read_groups_information() -> list:
    groups = pickle.load(open("groups.pickle", "rb"))
    specialties = []
    for group in groups:
        if group.specialty.name in specialties:
            continue
        specialties.append(group.specialty.name)
    return specialties


def read_students_information() -> list:
    students = pickle.load(open("students.pickle", "rb"))
    result = []
    for student in students:
        result.append(student)
    return result
