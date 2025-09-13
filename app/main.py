from datetime import datetime
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
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open('groups.pickle', 'wb') as file:
        file.write(pickle.dumps(groups))
    res = 0
    for group in groups:
        if len(group.students) > res:
            res = len(group.students)
    return res


def write_students_information(students: list[Student]) -> int:
    with open('students.pickle', 'wb') as file:
        file.write(pickle.dumps(students))
    return len(students)


def read_groups_information() -> list[str]:
    with open('groups.pickle', 'rb') as file:
        groups = pickle.load(file)
    return list({group.specialty.name for group in groups})


def read_students_information() -> list[Student]:
    with open('students.pickle', 'rb') as file:
        students = pickle.load(file)
    return students
