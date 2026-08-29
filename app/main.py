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


def write_groups_information(list_groups: list[Group]) -> int:
    max_students = []
    with open("groups.pickle", "wb") as f:
        for group in list_groups:
            max_students.append(len(group.students))
            pickle.dump(group, f)

    return max(max_students) if len(max_students) > 0 else []


def write_students_information(list_students: list[Student]) -> int:
    all_students = []
    with open("students.pickle", "wb") as f:
        for student in list_students:
            all_students.append(student)
            pickle.dump(student, f)
    return len(all_students)


def read_groups_information() -> list:
    name_specialty = []
    with open("groups.pickle", "rb") as inform_from_pickle:
        while True:
            try:
                group = pickle.load(inform_from_pickle)
                name_specialty.append(group.specialty.name)
            except EOFError:
                break
        need_return = list(set(name_specialty))
        if need_return is not None:
            return need_return
        return []


def read_students_information() -> list[Student]:
    list_students = []
    with open("students.pickle", "rb") as inform_from_pickle:
        while True:
            try:
                students = pickle.load(inform_from_pickle)
                list_students.append(students)
            except EOFError:
                break
        return list_students
