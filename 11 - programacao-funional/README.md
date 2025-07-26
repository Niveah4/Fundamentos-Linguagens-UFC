## Programação Funcional

### Introdução
A programação funcional é um paradigma que trata a computação como a avaliação de funções matemáticas, evitando estados e dados mutáveis. Dois conceitos essenciais nesse paradigma são:

- Funções de alta ordem: funções que recebem outras funções como argumento ou retornam funções.

- Recursão: técnica onde uma função chama a si mesma para resolver subproblemas menores.

### Problema:
- Encontrar números primos em uma lista e calcular o produto deles

Dada uma lista de inteiros, queremos identificar todos os números primos, elevar cada um deles a um valor (no caso aqui, podemos só usar o próprio número), e calcular o produto desses números primos.

### Solução em Python (programação funcional)

``` Python
from functools import reduce

def eh_primo(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return eh_primo(n, divisor + 1)

def produto_primos(lista):
    # Filtra apenas os números primos
    primos = filter(eh_primo, lista)
    # Calcula o produto dos números primos encontrados
    return reduce(lambda acc, x: acc * x, primos, 1)

# Exemplo de uso
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = produto_primos(numeros)
print(f"Produto dos números primos: {resultado}")
```

### Exemplo: Recursão simples para cálculo de potência

``` Python
def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

print(f"2 elevado a 5 é: {potencia(2, 5)}")
```

### Vantagens da Programação Funcional
A programação funcional oferece diversos benefícios, tornando-a uma escolha interessante para muitos problemas, especialmente aqueles que precisam de código limpo, modular e confiável. Destacam-se:

####  *Código mais expressivo e enxuto
O uso de funções puras e operações como filter e reduce ajuda a escrever lógicas complexas em poucas linhas, facilitando a leitura e manutenção.

####  *Melhor paralelização
Como funções funcionais não dependem de estados externos, elas podem ser executadas em paralelo com segurança, melhorando a performance em sistemas multi-core.

####  *Redução de efeitos colaterais
Funções puras sempre produzem os mesmos resultados para os mesmos inputs, evitando bugs ligados a estados mutáveis e compartilhados.

####  *Modularidade e reutilização
Funções são cidadãs de primeira classe, permitindo maior flexibilidade para criar componentes reutilizáveis e facilmente combináveis.

####  *Testabilidade facilitada
A previsibilidade das funções puras torna os testes mais simples e confiáveis, aumentando a qualidade geral do software.

