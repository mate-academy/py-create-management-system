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


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        return max(([len(student.students) for student in groups]), default=0)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        special_group = []
        for group in groups:
            special_group.append(group.specialty.name)
        special_group = list(set(special_group))
        return special_group


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        student_list = []
        students = pickle.load(f)
        for student in students:
            student_list.append(student)

        return student_list
