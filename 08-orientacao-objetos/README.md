# 08-orientacao-objetos

## Será feito modelado um Domínio de Transportes
- A hierarquia de veículos com uma classe base chamada Transporte e subclasses como Carro, Bicicleta e Avião.

## Conceitos Utilizados

- **Herança**: Classes específicas herdam comportamentos da classe base.
- **Polimorfismo**: Métodos com o mesmo nome se comportam de forma diferente em subclasses.
- **Encapsulamento**: Organização de atributos e métodos que representam comportamentos distintos de cada transporte.

## Classe Base: `Transporte`

```Java
class Transporte:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print(f"O {self.modelo} está se movendo.")

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
 ```

## Subclasse: `Bicicleta`

```Java
class Bicicleta(Transporte):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Ex: 'mountain bike', 'urbana'

    def mover(self):
        print(f"A bicicleta {self.modelo} está pedalando.")

    def exibir_info(self):
        super().exibir_info()
        print(f"Tipo: {self.tipo}")
```

## Subclasse: `Aviao`

```Java
class Aviao(Transporte):
    def __init__(self, marca, modelo, capacidade):
        super().__init__(marca, modelo)
        self.capacidade = capacidade

    def mover(self):
        print(f"O avião {self.modelo} está voando.")

    def exibir_info(self):
        super().exibir_info()
        print(f"Capacidade: {self.capacidade} passageiros")
```

## Exemplo de Uso


```Python
carro1 = Carro("Toyota", "Corolla", 4)
bike1 = Bicicleta("Caloi", "Elite", "mountain bike")
aviao1 = Aviao("Boeing", "747", 416)

transportes = [carro1, bike1, aviao1]

for t in transportes:
    t.exibir_info()
    t.mover()
    print("-" * 30)
```

## Resultados Esperados

```Python
Marca: Toyota | Modelo: Corolla
Número de portas: 4
O carro Corolla está dirigindo na estrada.
------------------------------
Marca: Caloi | Modelo: Elite
Tipo: mountain bike
A bicicleta Elite está pedalando.
------------------------------
Marca: Boeing | Modelo: 747
Capacidade: 416 passageiros
O avião 747 está voando.
------------------------------
```