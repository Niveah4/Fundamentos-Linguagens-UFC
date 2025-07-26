# 06-subprogramas

# Subprogramas: Passagem de Parâmetros por Valor e por Referência

# 1. Linguagem C

Em C, a passagem por valor é o comportamento padrão. Para simular passagem por referência, utilizamos ponteiros.

### Passagem por Valor (C)

```c
#include <stdio.h>

void alteraValor(int x) {
    x = 100;
    printf("Dentro da função (valor): x = %d\n", x);
}

int main() {
    int a = 10;
    alteraValor(a);
    printf("Fora da função: a = %d\n", a);
    return 0;
}
```
### saida esperada
```c
Dentro da função (valor): x = 100  
Fora da função: a = 10
```

## Passagem por Referência (C)

```c
#include <stdio.h>

void alteraReferencia(int *x) {
    *x = 100;
    printf("Dentro da função (referência): x = %d\n", *x);
}

int main() {
    int a = 10;
    alteraReferencia(&a);
    printf("Fora da função: a = %d\n", a);
    return 0;
}
```
### saida esperada
```c
Dentro da função (referência): x = 100  
Fora da função: a = 100
```

# 2. Python

Em Python, os objetos são passados por **atribuição de referência**. Isso significa que os parâmetros são referências para os objetos passados, mas o comportamento varia conforme o tipo do objeto:

- **Tipos imutáveis** (como `int`, `float`, `str`, `tuple`) se comportam como se fossem passados **por valor**, pois não podem ser alterados dentro da função.
- **Tipos mutáveis** (como `list`, `dict`, `set`) se comportam como se fossem passados **por referência**, pois podem ser modificados dentro da função.

### Exemplo com tipo imutável (int)

```python
def altera_valor(x):
    x = 100
    print(f"Dentro da função (valor): x = {x}")

a = 10
altera_valor(a)
print(f"Fora da função: a = {a}")

```

### saida esperada
```python
Dentro da função (valor): x = 100  
Fora da função: a = 10
```
### Exemplo com tipo mutável (list)

```python
def altera_lista(lst):
    lst[0] = 100
    print(f"Dentro da função (referência): lst = {lst}")

a = [10, 20, 30]
altera_lista(a)
print(f"Fora da função: a = {a}")
```

### saida esperada

```python
Dentro da função (referência): lst = [100, 20, 30]  
Fora da função: a = [100, 20, 30]
```

## Conclusão

| Linguagem | Tipo de Passagem               | Efeito Fora da Função | Obs                                                                 |
|-----------|--------------------------------|------------------------|----------------------------------------------------------------------------|
| C         | Valor (padrão)                 | Não                   | A variável original não é alterada; uma cópia é usada na função.          |
| C         | Referência (com ponteiros)     | Sim                   | A função altera o valor no endereço da variável original (uso de ponteiros). |
| Python    | Valor (imutáveis)              | Não                   | Objetos como int/str não podem ser alterados; a função usa uma nova cópia. |
| Python    | Referência (mutáveis)          | Sim                   | Listas/dicionários podem ser alterados diretamente dentro da função.      |
