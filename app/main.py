# Importações necessárias para o
# funcionamento do código

import dataclasses
from datetime import date
from typing import List
import pickle


# Representa uma especialidade lyceum
# Classe definida como imutável
@dataclasses.dataclass(frozen=True)
class Specialty:
    name: str
    number: int


# Representa um estudante lyceum
# Classe mutável por padrão
@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


# Representa um grupo de estudantes
# Classe mutável por padrão
# Uso a instância da classe Specialty
# Uso uma lista de estudantes instanciada da classe Student
@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


# Grava todas as informações dos grupo no arquivo groups.pickle
# Retorna o maior numero de estudantes entre todos os grupos
# e se caso a lista esteja vazia, retorna 0
def write_groups_information(
        groups: List[Group]
) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max((len(group.students) for group in groups), default=0)


# Grava todas as informações dos estudantes no arquivo students.pickle
# Recebe como parâmetro uma lista de instâncias da classe Student
# Retorna a quantidade total de estudantes gravados no arquivo
def write_students_information(
        students: List[Student]
) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


# Aqui vamos ler o dados do arquivo groups.pickle
# E vamos retornar uma lista ordenada com os nomes
# das especialidades, sem repetição e se caso o arquivo
# não exista, retorna uma lista vazia
def read_groups_information() -> List[Group]:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
    except FileNotFoundError:
        return []

    specialty_names = {group.specialty.name for group in groups}
    return sorted(specialty_names)


# Lê os dados do arquivo students.pickle
# Retorna uma lista de instancias da classe Student
# E se caso o arquivo nao exista, retorna uma lista vazia
def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
    except FileNotFoundError:
        return []

    return students
