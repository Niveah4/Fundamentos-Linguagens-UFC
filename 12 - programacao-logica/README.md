# 12 - Programação Lógica

# Problema: Relações de Família

Foi modelo um problema lógico simples usando Prolog, focado em **`relações de parentesco em uma familia`** como **pai**, **mãe**, **filho**, **avô** e **irmão**. Ele permite executar consultas para descobrir como os membros da família se conectam.

# Consultas:
- `?- avo(joao, ana).`
- `?- irmao(pedro, maria)`
- `?- filho(ana, ana_clara)`

# Código

```
:- discontiguous pai/2.
:- discontiguous mae/2.

% Base de dados
pai(joao, pedro).
pai(pedro, ana).
mae(maria, pedro).
mae(ana_clara, ana).

homem(joao).
homem(pedro).
mulher(maria).
mulher(ana_clara).
mulher(ana).

% Regras do problema

filho(X, Y) :- pai(Y, X).
filho(X, Y) :- mae(Y, X).

avo(X, Z) :- pai(X, Y), pai(Y, Z).
avo(X, Z) :- pai(X, Y), mae(Y, Z).

irmao(X, Y) :- pai(P, X), pai(P, Y), mae(M, X), mae(M, Y), X \= Y.
```
> Obs: Em Prolog, por padrão, todas as cláusulas de um mesmo predicado devem estar agrupadas — ou seja, não intercaladas com outros predicados, por isso uso do `:- discontiguous`.