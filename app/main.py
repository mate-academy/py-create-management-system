import pickle
import dataclasses


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
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    max_students_num = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    for group in group_list:
        if len(group.students) > max_students_num:
            max_students_num = len(group.students)
    return max_students_num


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_groups_information() -> str:
    list1 = []
    with open("groups.pickle", "rb") as f:
        for group in pickle.load(f):
            list1.append(group.specialty.name)
    return set(list1)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
