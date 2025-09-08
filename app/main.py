import dataclasses
import pickle
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Especialidade:
    name: str
    number: int


@dataclasses.dataclass
class Estudante:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Grupo:
    specialty: Especialidade
    course: int
    students: List[Estudante]


# --- Funções com pickle ---

def informacoes_de_grupos_de_gravacao(groups: List[Grupo]) -> int:
    """Grava os grupos em groups.pickle e retorna o maior número de alunos entre eles"""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    # calcula o máximo de alunos
    max_students = max((len(group.students) for group in groups), default=0)
    return max_students


def escrever_informacoes_para_os_alunos(students: List[Estudante]) -> int:
    """Grava todos os alunos em students.pickle e retorna a quantidade"""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def informacoes_de_grupos_de_leitura() -> List[str]:
    """Lê groups.pickle e retorna nomes de especialidades sem repetição"""
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def ler_informacoes_para_os_alunos() -> List[Estudante]:
    """Lê students.pickle e retorna lista de instâncias de Estudante"""
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
