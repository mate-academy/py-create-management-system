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


def write_groups_information(
        groups: list[Group]
) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    max_students = 0
    for group in groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(
        students: list[Student]
) -> int:
    with open("students.pickle", "wb") as file2:
        pickle.dump(students, file2)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file1:
        groups = pickle.load(file1)
    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file3:
        students = pickle.load(file3)
    return students
