from dataclasses import dataclass

@dataclass
class Filiale:
    id: int
    codice: str
    nome: str
    citta: str
    provincia: str
    latitudine: float
    longitudine: float

    def __eq__(self, other):
        return isinstance(other, Filiale) and self.id == other.id

    def __str__(self):
        return f"{self.nome} ({self.provincia})"

    def __repr__(self):
        return f"{self.nome} ({self.provincia})"

    def __hash__(self):
        return hash(self.id)

    #hash serve perchè se i due elementi confrontati nell eq sono uguali ma hanno hash
    #(ovvero come sono stati memorizzati) diversi, allora def hash serve a dire che se
    #gli id (nel caso di sto eq) sono uguali allora anche gli hash(ovvero come vengono
    #salvati) devono essere uguali, perchè se l'id è uguale rappresentano lo stesso
    #elemento
