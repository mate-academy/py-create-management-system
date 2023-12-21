import dataclasses as dc
from datetime import datetime
import pickle


@dc.dataclass
class Specialty:
    name: str
    number: int


@dc.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dc.dataclass
class Group:
    course: int
    specialty: Specialty
    students: list[Student]


def write_groups_information(groups: list[Group]):
    with open('groups.pickle', 'wb') as f:
        pickle.dump(groups, f)
        max_students_in_group = 0
        for group in groups:
            if len(group.students) > max_students_in_group:
                max_students_in_group = len(group.students)
                return max_students_in_group


def write_students_information(students: list[Student]):
    with open('students.pickle', 'wb') as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information():
    with open('groups.pickle', 'rb') as f:
        groups = pickle.load(f)
        return set(groups) if len(groups) else []


def read_students_information():
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
        return set(students) if len(students) else []


first_student = Student("Ivan", "Ivanov", "01.01.2001",
                        4.5, True, "123456789", "Moscow")

print(type(first_student))
