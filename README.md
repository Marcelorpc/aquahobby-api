# Aquahobby API 

Esta API tem como finalidade cadastrar, editar, visualizar e remover aquários e seus respectivos parâmetros, como:

* Nome

* Volume (L)

* Temperatura (°C)

* pH


## 1 - Preparando o ambiente

Para rodar este projeto localmente, é necessário que todas as bibliotecas Python listadas no arquivo requirements.txt estejam devidamente instaladas.

Após clonar o repositório, acesse o diretório raiz pelo terminal para executar os comandos descritos a seguir.

> É altamente recomendado utilizar ambientes virtuais para isolar as dependências do projeto e manter seu ambiente de desenvolvimento organizado.
Uma das formas mais comuns é utilizar o virtualenv ou o módulo venv do próprio Python.

Para criar um ambiente virtual no VS Code (ou outro terminal), utilize o seguinte comando:
```
python -m venv venv
```
Esse comando criará uma pasta chamada venv, que conterá todo o ambiente virtual.
Em seguida, ative o ambiente com:
```
.\venv\Scripts\activate
```
Com o ambiente ativado, você verá algo como (venv) antes da linha de comando — isso indica que as bibliotecas instaladas a partir deste ponto serão isoladas nesse ambiente. A partir daí, você pode seguir com a instalação das dependências via:
```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.



## 2 - Executando o projeto

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```


## 3 - Acessando a documentação

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## 4 - Tecnologias utilizadas

### Linguagem de Programação
• Python

### Framework Web
• Flask ==2.1.3 – microframework para construção da API

### CORS
• Flask-Cors ==3.0.10 – habilita o compartilhamento de recursos entre diferentes origens (CORS)

### Documentação OpenAPI
• flask-openapi3 ==2.1.0 – integração do Flask com especificações OpenAPI 3.0

### Validação de Dados
• Pydantic ==1.10.21 – validação e serialização de dados usando Python type hints

### ORM e Banco de Dados
• Flask-SQLAlchemy ==2.5.1 – integração do SQLAlchemy com o Flask
<br><br>
• SQLAlchemy ==1.4.41 – ORM para mapeamento objeto-relacional
<br><br>
• SQLAlchemy-Utils ==0.38.3 – extensões e utilitários para o SQLAlchemy
<br><br>
• SQLite – banco de dados leve e embutido, usado para persistência local

### Utilitários
• typing_extensions ==4.3.0 – recursos de tipagem para versões anteriores do Python
<br><br>
• Werkzeug ==2.0.3 – biblioteca WSGI utilizada internamente pelo Flask

## 5 - Funcionalidades Desenvolvidas

### Documentação da API
- **`GET /`**  
  Redireciona para a interface `/openapi`, onde o usuário pode escolher entre Swagger, Redoc ou RapiDoc para visualizar a documentação da API.

---

### Rotas da API

#### Adicionar Aquário
- **`POST /aquario`**  
  Adiciona um novo aquário à base de dados.  
  Requer os seguintes campos no corpo da requisição:
  - `nome` (str)
  - `volume` (int)
  - `temperatura` (float)
  - `ph` (float)  
  **Resposta:** retorna o aquário criado com sucesso ou erro se o nome já existir.

#### Listar Todos os Aquários
- **`GET /aquarios`**  
  Retorna a lista de todos os aquários cadastrados na base.  
  **Resposta:** lista de aquários ou lista vazia caso não haja nenhum.

#### Buscar Aquário por Nome
- **`GET /aquario?nome=...`**  
  Busca e retorna um aquário específico a partir do nome informado.  
  **Resposta:** detalhes do aquário ou erro 404 se não encontrado.

#### Remover Aquário por Nome
- **`DELETE /aquario?nome=...`**  
  Remove um aquário da base de dados pelo nome.  
  **Resposta:** mensagem de confirmação da remoção ou erro 404 se não encontrado.

#### Atualizar Aquário
- **`PUT /aquario?nome=...`**  
  Atualiza os dados de um aquário existente.  
  Campos possíveis no corpo da requisição:
  - `nome` (str)
  - `volume` (int)
  - `temperatura` (float)
  - `ph` (float)  
  **Resposta:** retorna o aquário atualizado com sucesso ou erro se não encontrado ou falha na atualização.
