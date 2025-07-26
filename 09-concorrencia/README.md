# 09-concorrencia

## Diferença entre Threads e Processos

| Característica      | Thread                                         | Processo                                      |
|---------------------|-----------------------------------------------|-----------------------------------------------|
| Definição           | Menor unidade de execução dentro de um processo | Programa em execução, com sua própria memória |
| Compartilhamento    | Compartilham a mesma memória do processo pai   | Têm memória isolada                           |
| Comunicação         | Mais simples e rápida                          | Mais complexa (requer IPC: pipes, sockets)    |
| Criação             | Leve e rápida                                  | Mais pesada e lenta                           |
| Falha               | Pode afetar outras threads                     | Isolada — falha de um processo não afeta outro|

---

## Exemplo Personalizado em Python

### Contexto:
Simulando **duas tarefas concorrentes**:
- Uma tarefa imprime números pares
- Outra imprime números ímpares  
Cada uma roda em **thread** ou em **processo separado**

---

### 1. Usando `threading` (compartilham memória)

```python
import threading
import time

def imprimir_pares():
    for i in range(0, 10, 2):
        print(f"[Pares] {i}")
        time.sleep(0.5)

def imprimir_impares():
    for i in range(1, 10, 2):
        print(f"[Ímpares] {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    t1 = threading.Thread(target=imprimir_pares)
    t2 = threading.Thread(target=imprimir_impares)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Finalizado com threads.")

## Usando `multiprocessing` (isolamento de memória)

```python
import multiprocessing
import time

def imprimir_pares():
    for i in range(0, 10, 2):
        print(f"[Pares] {i}")
        time.sleep(0.5)

def imprimir_impares():
    for i in range(1, 10, 2):
        print(f"[Ímpares] {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=imprimir_pares)
    p2 = multiprocessing.Process(target=imprimir_impares)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finalizado com processos.")
```

## Saída Esperada (aproximada)
```python
[Pares] 0
[Ímpares] 1
[Pares] 2
[Ímpares] 3
...
[Pares] 8
[Ímpares] 9

```

---

## Quando usar cada um?

| Quando usar Threads                           | Quando usar Processos                         |
|-----------------------------------------------|-----------------------------------------------|
| Tarefas com muito compartilhamento de dados   | Tarefas isoladas com risco de travamento      |
| Operações de I/O (leitura, espera)            | Operações pesadas de CPU                      |
| Requer baixa sobrecarga                       | Requer segurança entre tarefas                |


