# Sistema de Login Básico

Este repositório contém um sistema de login básico implementado em Python.

## Descrição

O sistema de login permite que os usuários se registrem, façam login e logout. Ele mantém uma lista de usuários e senhas, bem como uma lista de usuários atualmente logados.

## Como usar

O sistema de login é implementado como uma função chamada `implementAPI`. Esta função aceita uma lista de logs, onde cada log é uma lista que representa uma ação do usuário. Cada ação do usuário deve ser uma das seguintes:

- 'register': Registra um novo usuário. Deve ser seguido pelo nome de usuário e senha.
- 'login': Faz login de um usuário. Deve ser seguido pelo nome de usuário e senha.
- 'logout': Faz logout de um usuário. Deve ser seguido pelo nome de usuário.

A função `implementAPI` retorna uma lista de resultados para cada ação do usuário.

## Exemplo

Aqui está um exemplo de como usar a função `implementAPI`:

```python
logs = [['register', 'david', 'david123'], ['register', 'adam', '1Adam1'], ['login', 'david', 'david123'], ['login' ,'adam', '1adam1'],['logout', 'david']]
print(implementAPI(logs))
