from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Aquario
from schemas import *
from flask_cors import CORS

info = Info(title="Aquahobby API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aquario_tag = Tag(name="Aquário", description="Adição, visualização e remoção de aquários da base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/aquario', tags=[aquario_tag],
          responses={"200": AquarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aquario(body: AquarioSchema):
    """Adiciona um novo Aquario à base de dados

    Retorna uma representação do aquário.
    """

    aquario = Aquario(
        nome= body.nome,
        volume= body.volume,
        temperatura= body.temperatura,
        ph= body.ph
        )
    try:
        session = Session()
        session.add(aquario)
        session.commit()
        return apresenta_aquario(aquario), 200

    except IntegrityError as e:
        error_msg = "Aquário de mesmo nome já salvo na base"
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item"
        return {"message": error_msg}, 400


@app.get('/aquarios', tags=[aquario_tag],
         responses={"200": ListagemAquariosSchema, "404": ErrorSchema})
def get_aquarios():
    """Faz a busca por todos os Aquários cadastrados

    Retorna uma representação da listagem dos aquários.
    """
    session = Session()
    aquarios = session.query(Aquario).all()

    if not aquarios:
        return {"aquarios": []}, 200
    else:
        return apresenta_aquarios(aquarios), 200


@app.get('/aquario', tags=[aquario_tag],
         responses={"200": AquarioViewSchema, "404": ErrorSchema})
def get_aquario(query: AquarioBuscaSchema):
    """Faz a busca por um Aquário a partir do nome do aquário

    Retorna uma representação dos aquários.
    """
    aquario_nome = query.nome
    session = Session()
    aquario = session.query(Aquario).filter(Aquario.nome == aquario_nome).first()

    if not aquario:
        error_msg = "Aquário não encontrado na base"
        return {"message": error_msg}, 404
    else:
        return apresenta_aquario(aquario), 200


@app.delete('/aquario', tags=[aquario_tag],
            responses={"200": AquarioDelSchema, "404": ErrorSchema})
def del_aquario(query: AquarioBuscaSchema):
    """Deleta um Aquário a partir do nome do aquário informado

    Retorna uma mensagem de confirmação da remoção.
    """
    aquario_nome = unquote(unquote(query.nome))
    print(aquario_nome)
    session = Session()
    count = session.query(Aquario).filter(Aquario.nome == aquario_nome).delete()
    session.commit()

    if count:
        return {"message": "Aquário removido", "id": aquario_nome}
    else:
        error_msg = "Aquário não encontrado na base"
        return {"message": error_msg}, 404


@app.put('/aquario', tags=[aquario_tag],
         responses={"200": AquarioViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_aquario(query: AquarioBuscaSchema, body: AquarioUpdateSchema):
    """Atualiza um aquário existente na base de dados

    Retorna a representação do aquário atualizado.
    """
    session = Session()
    aquario = session.query(Aquario).filter(Aquario.nome == query.nome).first()

    if not aquario:
        error_msg = "Aquário não encontrado na base"
        return {"message": error_msg}, 404

    # Atualiza apenas os campos fornecidos no form
    if body.nome is not None:
        aquario.nome = body.nome
    if body.volume is not None:
        aquario.volume = body.volume
    if body.temperatura is not None:
        aquario.temperatura = body.temperatura
    if body.ph is not None:
        aquario.ph = body.ph

    try:
        session.commit()
        return apresenta_aquario(aquario), 200

    except Exception as e:
        error_msg = f"Erro ao atualizar o aquário: {str(e)}"
        return {"message": error_msg}, 400