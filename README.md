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
