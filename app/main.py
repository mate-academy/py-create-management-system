from dataclasses import dataclass
from datetime import datetime
import pickle


# 1. Définition des structures de données (Dataclasses)

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
    students: list[Student]


# 2. Implémentation des fonctions de sérialisation / désérialisation

def write_groups_information(groups_list: list[Group]) -> int:
    """Enregistre les groupes dans groups.pickle et retourne le nombre maximal

    d'élèves parmi tous les groupes.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups_list, file)

    if not groups_list:
        return 0

    # Recherche du nombre d'étudiants maximal dans un groupe
    max_students = max(len(group.students) for group in groups_list)
    return max_students


def write_students_information(students_list: list[Student]) -> int:
    """Enregistre les étudiants dans students.pickle et retourne le nombre

    total d'étudiants enregistrés.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students_list, file)

    return len(students_list)


def read_groups_information() -> list[str]:
    """Lit les données de groups.pickle et renvoie la liste des noms

    des spécialités, sans doublons.
    """
    try:
        with open("groups.pickle", "rb") as file:
            groups_list = pickle.load(file)
    except FileNotFoundError:
        return []

    # Extraction des noms de spécialités uniques grâce à un ensemble (set)
    unique_specialties = {group.specialty.name for group in groups_list}

    return list(unique_specialties)


def read_students_information() -> list[Student]:
    """Lit les données de students.pickle et renvoie la liste

    de toutes les instances Student trouvées.
    """
    try:
        with open("students.pickle", "rb") as file:
            students_list = pickle.load(file)
    except FileNotFoundError:
        return []

    return students_list
