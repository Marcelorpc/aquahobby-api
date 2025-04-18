from pydantic import BaseModel
from typing import List, Optional
from model.aquario import Aquario

class AquarioSchema(BaseModel):
    """ Representa os dados de entrada para criação de um novo aquário
    """
    nome: str 
    volume: int 
    temperatura: float
    ph: float


class AquarioBuscaSchema(BaseModel):
    """ Estrutura que define os dados necessários para buscar um aquário pelo nome.
    """
    nome: str = ""


class ListagemAquariosSchema(BaseModel):
    """ Define a estrutura da resposta para a listagem de aquários.
    """
    aquarios:List[AquarioSchema]


class AquarioViewSchema(BaseModel):
    """ Define a estrutura de retorno dos dados de um aquário.
    """
    id: int 
    nome: str 
    volume: int 
    temperatura: float 
    ph: float 


class AquarioDelSchema(BaseModel):
    """ Define a estrutura de resposta após a exclusão de um aquário.
    """
    message: str
    nome: str

class AquarioUpdateSchema(BaseModel):
    """ Define os dados permitidos para atualização de um aquário 
    """
    nome: Optional[str] = ''
    volume: Optional[int]
    temperatura: Optional[float]
    ph: Optional[float]

def apresenta_aquarios(aquarios: List[Aquario]):
    """ Retorna uma lista de aquários conforme representação definida no schema AquarioViewSchema.
    """
    result = []
    for aquario in aquarios:
        result.append({
            "nome": aquario.nome,
            "volume": aquario.volume,
            "temperatura": aquario.temperatura,
            "ph": aquario.ph
        })

    return {"aquarios": result}


def apresenta_aquario(aquario: Aquario):
    """ Retorna um aquário conforme  definida no schema AquarioViewSchema.
    """
    return {
        "id": aquario.id,
        "nome": aquario.nome,
        "volume": aquario.volume,
        "temperatura": aquario.temperatura,
        "ph": aquario.ph
    }
