# write your code here
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student] = field(default_factory=list)


def write_groups_information(groups: List[Group]) -> int:
    """Сохраняет информацию о группах в файл 'groups.pickle' и возвращает
    максимальное количество студентов в группе.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def write_students_information(students: List[Student]) -> int:
    """Сохраняет информацию обо всех студентах в файл 'students.pickle' и
    возвращает общее количество студентов.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    """Считывает информацию о группах из 'groups.pickle' и
    возвращает уникальные названия специализаций.
    """
    try:
        with open("groups.pickle", "rb") as f:
            groups: List[Group] = pickle.load(f)
        unique_specialties = list({group.specialty.name for group in groups})
        return unique_specialties
    except FileNotFoundError:
        return []


def read_students_information() -> List[Student]:
    """Считывает информацию о студентах из 'students.pickle'
    и возвращает список студентов.
    """
    try:
        with open("students.pickle", "rb") as f:
            students: List[Student] = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
