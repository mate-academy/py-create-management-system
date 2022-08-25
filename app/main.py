import dataclasses
import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: Student


def write_groups_information(groups: list):
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if len(groups) == 0:
        return 0
    return max([len(group.students) for group in groups])


def write_students_information(students: list):
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return {group.specialty.name for group in groups}


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
