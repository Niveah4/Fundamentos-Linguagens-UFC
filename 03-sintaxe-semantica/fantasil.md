
# Fantasil - Relatório do Desafio 03

## 1. Introdução
Este projeto apresenta a linguagem **Fantasil**, desenvolvida como parte do Desafio 03 da disciplina de Linguagens de Programação. O objetivo é demonstrar a aplicação de conceitos teóricos na criação de uma gramática fictícia, incluindo análises léxica e sintática.

## 2. Especificações da Linguagem

### 2.1 Componentes Léxicos

| Categoria           | Exemplos                          |
|---------------------|-----------------------------------|
| Palavras-reservadas | `conjurar`, `se`, `senao`, `enquanto`, `int`, `texto` |
| Elementos mágicos   | `fogo`, `agua`, `terra`, `ar`     |
| Operadores          | `+`, `->`, `==`, `>=`             |
| Literais            | `10`, `"raio"`, `verdadeiro`, `falso` |
| Delimitadores       | `()`, `{}`, `;`                   |

### 2.2 Estrutura Básica

#### Declaração de Feitiço

```fantasil
conjurar <nome>(<tipo> <parametro>) {
    <comandos>;
}
```

**Exemplo Completo**:

```fantasil
conjurar ataque(int poder) {
    se (poder >= 5) {
        fogo -> "inferno";
    } senao {
        ar -> "ventania";
    }
}
```

## 3. Análise Léxica

### 3.1 Exemplo de Tokenização

**Código**:

```fantasil
enquanto (mana > 0) { conjurar cura(5); }
```

**Tokens Gerados**:

| Lexema     | Categoria         |
|------------|-------------------|
| enquanto   | Palavra-reservada |
| (          | Delimitador       |
| mana       | Identificador     |
| >          | Operador          |
| 0          | Literal           |
| {          | Delimitador       |
| conjurar   | Palavra-reservada |
| cura       | Identificador     |
| (          | Delimitador       |
| 5          | Literal           |
| )          | Delimitador       |
| ;          | Delimitador       |
| }          | Delimitador       |

## 4. Análise Sintática

### 4.1 Gramática BNF

```
<Programa> ::= <Feitiço>+
<Feitiço> ::= "conjurar" <ID> "(" <Parametros> ")" "{" <Comandos> "}"
<Parametros> ::= <Parametro> ("," <Parametro>)* | ε
<Parametro> ::= <Tipo> <ID>
<Tipo> ::= "int" | "texto"
<Comandos> ::= <Comando>+
<Comando> ::= <Chamada> | <Condicional> | <Loop> | <Atribuicao>
<Condicional> ::= "se" "(" <Condicao> ")" "{" <Comandos> "}" ["senao" "{" <Comandos> "}"]
<Loop> ::= "enquanto" "(" <Condicao> ")" "{" <Comandos> "}"
```

### 4.2 Árvore Sintática

Para o código:

```fantasil
enquanto (mana > 0) { conjurar cura(5); }
```

**Estrutura**:

```
<Programa>
  └─ <Feitiço>
       └─ <Comando>
            └─ <Loop>
                 ├─ <Condicao>
                 │    ├─ mana
                 │    ├─ >
                 │    └─ 0
                 └─ <Bloco>
                      └─ <Chamada>
                           ├─ conjurar
                           ├─ cura
                           └─ 5
```

## 5. Análise Semântica

### 5.1 Regras de Validação

1. Tipos incompatíveis não podem ser combinados.
2. Variáveis devem ser declaradas antes do uso.
3. Estruturas de controle devem retornar valores booleanos.

### 5.2 Tabela de Combinações

| Combinação         | Resultado   |
|--------------------|-------------|
| fogo + agua        | vapor       |
| terra + ar         | poeira      |

## 6. Conclusão
A linguagem Fantasil demonstra a aplicação prática dos conceitos estudados na disciplina de Linguagens de Programação, especialmente nas áreas de análise léxica, sintática e semântica.

## 7. Referências

- AHO, A. V. et al. *Compiladores: princípios, técnicas e ferramentas*.
- Material didático da disciplina.
