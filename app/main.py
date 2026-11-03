import dataclasses
from datetime import datetime
import pickle

@dataclasses.dataclass
class Especialidade:
    name: str
    number: str  # Pode ser str ou int dependendo de como o código numérico for estruturado

@dataclasses.dataclass
class Estudante:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float  # Média das notas
    has_scholarship: bool  # Se possui bolsa de estudos
    phone_number: str
    address: str

@dataclasses.dataclass
class Grupo:
    specialty: Especialidade
    course: int  # Número do curso / ano de estudo
    students: list[Estudante]  # Lista de alunos matriculados

def escrever_informações_de_grupos(groups: list[Grupo]) -> int:
    """
    Grava todas as instâncias de Grupo no arquivo 'groups.pickle' 
    e retorna o número máximo de alunos entre todos os grupos.
    """
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            
    if not groups:
        return 0
    return max(len(group.students) for group in groups)

def escrever_informações_dos_alunos(students: list[Estudante]) -> int:
    """
    Grava todas as instâncias de Estudante no arquivo 'students.pickle' 
    e retorna o número total de alunos.
    """
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
            
    return len(students)

def ler_informações_dos_grupos() -> list[str]:
    """
    Lê os dados do arquivo 'groups.pickle' e retorna uma lista 
    com os nomes de todas as especialidades, sem repetição.
    """
    groups = []
    try:
        with open("groups.pickle", "rb") as f:
            while True:
                try:
                    groups.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []
    
    # Utiliza um conjunto (set) para garantir nomes únicos de especialidades
    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)

def ler_informações_dos_alunos() -> list[Estudante]:
    """
    Lê os dados do arquivo 'students.pickle' e retorna 
    uma lista com todas as instâncias da classe Estudante.
    """
    students = []
    try:
        with open("students.pickle", "rb") as f:
            while True:
                try:
                    students.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return []
        
    return students
