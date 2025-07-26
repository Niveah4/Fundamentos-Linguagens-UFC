
# 08 - Tipos de Dados

## Comparação de Tipagem: Java, Python e C

Nesta seção, comparamos como a tipagem de variáveis funciona em três linguagens populares: **Java**, **Python** e **C**. A tipagem se refere a como os tipos de dados são declarados e utilizados em uma linguagem.

### 1. Comparação Geral

| Linguagem | Tipagem            | Verificação  | Exemplo                        |
|-----------|--------------------|--------------|--------------------------------|
| **Java**  | Estática, forte     | Em tempo de compilação | `int idade = 20;`              |
| **C**     | Estática, fraca     | Em tempo de compilação | `int idade = 20;`              |
| **Python**| Dinâmica, forte     | Em tempo de execução   | `idade = 20`                   |

>  *Tipagem estática* exige declaração de tipo explícito.  
>  *Tipagem dinâmica* permite mudar o tipo durante a execução.  
>  *Tipagem forte* não permite conversão implícita de tipos incompatíveis.  
>  *Tipagem fraca* pode permitir conversões implícitas arriscadas.

---

### Comparativo de forma detalhada:

| Característica                 | **Java**                               | **C**                                   | **Python**                               |
|-------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|
| **Tipo de Tipagem**           | Estática e Forte                       | Estática e Fraca                         | Dinâmica e Forte                         |
| **Declaração de Tipo**        | Obrigatória                            | Obrigatória                              | Opcional (inferência automática)         |
| **Verificação de Tipos**      | Em tempo de compilação                 | Em tempo de compilação (menos rígida)    | Em tempo de execução                     |
| **Conversões Implícitas**     | Não permite (sem casting)              | Permite (com possíveis erros)            | Não permite entre tipos incompatíveis    |
| **Mutabilidade de Tipo**      | Não muda após atribuição               | Não muda após atribuição                 | Pode mudar ao longo do código            |
| **Exemplo de Tipos Primitivos**| `int`, `float`, `char`, `boolean`     | `int`, `float`, `char`, `bool` (com lib)| `int`, `float`, `str`, `bool`            |
| **Tipos de Referência**       | Classes, Interfaces, Arrays           | Ponteiros                                | Objetos, listas, dicionários, classes    |
| **Segurança de Tipo**         | Alta                                   | Baixa                                    | Alta                                     |


### 2. Exemplos Comentados

####  Java (tipagem estática e forte)

```java
int idade = 20;          // tipo precisa ser declarado
String nome = "Maria";   // erro se tentar fazer nome = 20
```

####  C (tipagem estática e fraca)

```c
int idade = 20;          // tipo também precisa ser declarado
idade = "vinte";         // erro em compilação
printf("%d", 3 + 'a');   // operação permitida (resultado: 100, pois 'a' = 97)
```

####  Python (tipagem dinâmica e forte)

```python
idade = 20              // tipo não precisa ser declarado
idade = "vinte"         // permitido, mas o tipo muda
print(idade + 5)        // erro em tempo de execução (str + int)
```

---

### 3. Conclusão

- **Java** e **C** exigem que o tipo seja definido antes do uso, o que ajuda na detecção de erros na compilação.
- **Python** é mais flexível, mas erros de tipo aparecem só durante a execução.
- A escolha entre linguagens de tipagem estática ou dinâmica depende do contexto: segurança vs. flexibilidade.
