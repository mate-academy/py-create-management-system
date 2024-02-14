import dataclasses
import datetime
import pickle


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Specialty:
    name: str
    number: int


@dataclasses.dataclass(frozen=True, eq=True, order=True)
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
    students: list


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    count_students = set()
    for group in groups:
        for student in group.students:
            count_students.add(student)
    return len(count_students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        groups_specialty = list({groups.specialty.name for groups in groups})
    return groups_specialty


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        students_list = [student for student in students]
    return students_list
