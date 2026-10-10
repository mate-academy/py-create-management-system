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
    course: int
    students: list[Student]


def write_groups_information(groups: Group) -> int:
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: Student) -> int:
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
        return len(students)


def read_groups_information() -> list:
    list_groups = []
    with open("groups.pickle", "rb") as f:
        while True:
            try:
                list_groups.append(pickle.load(f))
            except EOFError:
                break
    return list({group.specialty.name for group in list_groups})


def read_students_information() -> list:
    list_students = []
    with open("students.pickle", "rb") as f:
        while True:
            try:
                list_students.append(pickle.load(f))
            except EOFError:
                break
    return list_students
