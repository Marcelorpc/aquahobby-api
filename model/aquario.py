from sqlalchemy import Column, String, Integer, Float

from  model import Base

class Aquario(Base):
    __tablename__ = 'Aquário'

    id = Column("pk_aquario", Integer, primary_key=True)
    nome = Column(String(60), unique=True)
    volume = Column(Integer)
    temperatura = Column(Float)
    ph = Column(Float)

    def __init__(self, nome:str, volume:int, temperatura:float, ph:float):
        """
        Cria um Aquário

        Arguments:
            nome: nome do aquário.
            volume: Capacidade em litros do aquário
            temperatura: Temperatura média do aquário
            ph: Ph médio do aquário
        """
        self.nome = nome
        self.volume = volume
        self.temperatura = temperatura
        self.ph = ph
