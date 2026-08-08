from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[object]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    for check in group_list:
        if check.__getattribute__("students") is not None:
            return max([len(i.__getattribute__("students"))
                        for i in group_list])


def write_students_information(students_list: list) -> int:
    count_students = 0
    for i in students_list:
        i.__getattribute__("first_name")
        count_students += 1
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return count_students


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    return set(i.__getattribute__("specialty").name for i in groups)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return list(students)
