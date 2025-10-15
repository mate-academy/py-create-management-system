import dataclasses
from datetime import datetime
from typing import List
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
    students: List[Student]


def write_groups_information(groups: List[Group]):
    """Salva os grupos no arquivo e retorna o maior número de estudantes."""
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    high = []
    for group in groups:
        high.append(len(group.students))
    return max(high)


def write_students_information(students: List[Student]):
    """Salva os estudantes no arquivo e retorna a quantidade total."""
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information(groups: List[Group]):
    """Lê os grupos do arquivo e retorna a lista de especialidades sem repetição."""
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    especialides = []
    for group in groups:
        if group.specialty.name not in especialides:
            especialides.append(group.specialty.name)

    return especialides


def read_students_information(students: List[Student]):
    """Lê os estudantes do arquivo e retorna a lista completa."""
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
