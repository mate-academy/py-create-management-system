import dataclasses
import pickle
from datetime import datetime


@dataclasses.dataclass(frozen=True)
class Specialty:
    """Reprezentuje specjalność w Lyceum."""
    name: str
    number: str


@dataclasses.dataclass
class Student:
    """Reprezentuje studenta Lyceum."""
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    """Reprezentuje grupę studentów przypisaną do specjalności i kursu."""
    specialty: Specialty
    course: int
    students: list = dataclasses.field(default_factory=list)  # Typ usunięty


# --- FUNKCJE ZAPISU (SERIALIZACJI) ---

def write_groups_information(groups: list) -> int:
    """
    Zapisuje informacje o grupach do pliku "groups.pickle".
    Zwraca maksymalną liczbę studentów w jednej grupie.
    """
    max_students = 0

    # 1. Obliczenie maksymalnej liczby studentów
    for group in groups:
        num_students = len(group.students)
        if num_students > max_students:
            max_students = num_students

    # 2. Zapis listy obiektów do pliku (bez try/except)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    return max_students


def write_students_information(students: list) -> int:
    """
    Zapisuje informacje o wszystkich studentach do pliku "students.pickle".
    Zwraca całkowitą liczbę zapisanych studentów.
    """
    total_students = len(students)

    # Zapis listy obiektów do pliku (bez try/except)
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return total_students


# --- FUNKCJE ODCZYTU (DESERIALIZACJI) ---

def read_groups_information() -> set:
    """
    Odczytuje dane z pliku "groups.pickle".
    Zwraca nazwy wszystkich specjalności bez powtórzeń.
    """
    groups = []

    # 1. Odczyt danych z pliku (bez try/except)
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

        # 2. Wyodrębnienie nazw specjalności
    specialty_names = set()
    for group in groups:
        # Zakładamy, że typy danych są poprawne
        specialty_names.add(group.specialty.name)

    return specialty_names


def read_students_information() -> list:
    """
    Odczytuje dane z pliku "students.pickle".
    Zwraca listę wszystkich instancji klasy Student.
    """
    students = []

    # 1. Odczyt danych z pliku (bez try/except)
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
