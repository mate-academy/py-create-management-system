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


def write_groups_information(groups: list[Group]) -> int:
    """Grava as instâncias de Group no arquivo 'groups.pickle'
    e retorna o número máximo de alunos entre todos os grupos."""
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    """Grava as instâncias de Student no arquivo 'students.pickle'
    e retorna o total de alunos."""
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)

    return len(students)


def read_groups_information() -> list[str]:
    """Lê os dados do arquivo 'groups.pickle' e retorna
    os nomes únicos de todas as especialidades dos grupos."""
    specialty_names = set()

    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    group = pickle.load(f)
                    specialty_names.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return list(specialty_names)


def read_students_information() -> list[Student]:
    """Lê os dados do arquivo 'students.pickle' e retorna
    uma lista com todas as instâncias de Student."""
    students = []

    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    student = pickle.load(f)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        return []

    return students
