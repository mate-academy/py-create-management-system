# write your code here
import dataclasses
from datetime import datetime
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
    course: str
    students: list[Student]


GROUP_INFO = "groups.pickle"
STUDENTS_INFO = "students.pickle"


def write_groups_information(groups: list[Group]) -> int:
    if len(groups) == 0:
        return 0
    with open(GROUP_INFO, "wb") as group_file:
        pickle.dump(groups, group_file)
    return max([len(group.students) for group in groups])


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_INFO, "wb") as student_file:
        pickle.dump(students, student_file)
    return len(students)


def read_groups_information() -> list:
    try:
        with open(GROUP_INFO, "rb") as group_file:
            groups = pickle.load(group_file)
            return [
                name for name in
                set(group.specialty.name for group in groups)
            ]
    except FileNotFoundError:
        return []


def read_students_information() -> list:
    with open(STUDENTS_INFO, "rb") as student_file:
        return pickle.load(student_file)
