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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        list_of_groups: list[Group]
) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(list_of_groups, groups_file)
    max_of_students = 0
    for group in list_of_groups:
        if len(group.students) > max_of_students:
            max_of_students = len(group.students)
    return max_of_students


def write_students_information(
        list_of_students: list[Student]
) -> int:
    with open("students.pickle", "wb") as students_file:
        pickle.dump(list_of_students, students_file)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as read_groups_file:
        groups = pickle.load(read_groups_file)
    specialties = set([group.specialty.name for group in groups])
    return specialties


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = []
        while True:
            try:
                student = pickle.load(f)
                students.append(student)
            except EOFError:
                break
    return [student for sublist in students for student in sublist]
