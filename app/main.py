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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups_file:
        pickle.dump(list_of_groups, groups_file)

    return max([len(group.students) for group in list_of_groups], default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_file:
        # for student in list_of_students:
        pickle.dump(list_of_students, students_file)

    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as groups_file:
        list_of_groups = pickle.load(groups_file)

        return list(set([group.specialty.name for group in list_of_groups]))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as students_file:
        list_of_students = pickle.load(students_file)

        return list_of_students
