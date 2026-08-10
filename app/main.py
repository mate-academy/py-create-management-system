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
    phone_number: bool
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    try:
        return max(len(group.students) for group in groups)
    except ValueError:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as f:
        list1 = pickle.load(f)
    return list({group.specialty.name for group in list1})


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        list1 = pickle.load(f)
    return list1
