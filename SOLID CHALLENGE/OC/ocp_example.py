from abc import ABC, abstractmethod

class AprovaExameInteface(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

    def verifica_condicoes_exame(self, exame):
        
        pass

class AprovaExameSangue(AprovaExameInteface):
    def aprovar_solicitacao_exame(self, exame):
        if exame.tipo == "sangue":
            if self.verifica_condicoes_exame(exame):
                print("Exame sanguíneo aprovado!")

    def verifica_condicoes_exame(self, exame):
        pass

class AprovaExameRaioX(AprovaExameInteface):
    def aprovar_solicitacao_exame(self, exame):
        if exame.tipo == "raio-x":
            if self.verifica_condicoes_exame(exame):
                print("Raio-X aprovado!")

    def verifica_condicoes_exame(self, exame):
        pass


class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovadorSangue = AprovaExameSangue()
aprovadorRaio = AprovaExameRaioX()

aprovadorSangue.aprovar_solicitacao_exame(exame_sangue)
aprovadorRaio.aprovar_solicitacao_exame(exame_raio_x)