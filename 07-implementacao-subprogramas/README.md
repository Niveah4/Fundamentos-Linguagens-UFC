# 07-implementacao-subprogramas

## Implementação de Subprogramas
➤ Exemplo Recursivo: Fatorial de um número

## Função recursiva em pseudocódigo:

``` python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
```

- Pilha de Chamadas (Call Stack)
Se chamarmos fatorial(3), a execução se dá em chamadas aninhadas, que são empilhadas na memória até chegar no caso base.

## Execução: fatorial(3)

### 
 Execução: `fatorial(3)`

| Etapa | Pilha de Chamadas (de baixo pra cima)                           | Ação                         |
|-------|------------------------------------------------------------------|------------------------------|
| 1     | `fatorial(3)`                                                   | `3 * fatorial(2)`            |
| 2     | `fatorial(3)`<br>`fatorial(2)`                                  | `2 * fatorial(1)`            |
| 3     | `fatorial(3)`<br>`fatorial(2)`<br>`fatorial(1)`                 | `1 * fatorial(0)`            |
| 4     | `fatorial(3)`<br>`fatorial(2)`<br>`fatorial(1)`<br>`fatorial(0)`| Caso base: retorna `1`       |

---

Após atingir o caso base (`fatorial(0)`), as funções começam a desempilhar:

- `fatorial(1)` retorna `1 * 1 = 1`
- `fatorial(2)` retorna `2 * 1 = 2`
- `fatorial(3)` retorna `3 * 2 = 6`

---

###  Explicação da Pilha

- Cada chamada recursiva é empilhada com seu próprio **contexto (variável `n`)**.
- A pilha cresce até atingir o **caso base**, depois começa a desempilhar resolvendo as chamadas anteriores.
- Se não houver um caso base, a pilha continua crescendo até estourar a memória → **erro de estouro de pilha (stack overflow)**.

## Visual da pilha durante a chamada de `fatorial(3)`

<img src="/07-implementacao-subprogramas/pilha.png" alt="Pilha de chamadas" width="100">



