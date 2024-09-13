# Projeto de API Matemática com FastAPI

Este projeto é uma API RESTful desenvolvida com FastAPI para realizar operações matemáticas simples. A API permite somar e calcular a média de uma lista de inteiros.

## Funcionalidades

- **Somar**: Calcula a soma dos números fornecidos em um vetor.
- **Média**: Calcula a média aritmética dos números fornecidos em um vetor.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:
```shell
    ├── app
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1.py
    │   ├── core
    │   │   └── __init__.py
    │   ├── domain
    │   │   ├── complex_number_library.py
    │   │   ├── __init__.py
    │   │   ├── interfaces.py
    │   │   └── services.py
    │   └── tests
    │       ├── __init__.py
    │       ├── test_number.py
    │       └── test_numbers.py
    ├── main.py
    ├── Makefile
    ├── poetry.lock
    ├── pyproject.toml
    └── README.md
```



## Como Rodar a API

Certifique-se de que todas as dependências estão instaladas e, em seguida, use o `Makefile` para iniciar a API.

### Instalação

Clone o repositório e instale as dependências com Poetry:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
poetry install
```

## para iniciar a API
    make run-api

A API estará disponível em http://localhost:8000.

A documentação da api está disponivel em http://localhost:8000/docs