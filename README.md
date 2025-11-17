# Sistema de Transporte – Exemplo de Herança em Python

Este projeto demonstra o uso de **herança** e **polimorfismo** em Python por meio de uma classe base (`Transporte`) e três subclasses (`Carro`, `Moto` e `Bicicleta`).
Cada classe sobrescreve o método `Mover` para representar seu próprio comportamento.

## Estrutura das Classes

* **Transporte**
  Classe base que armazena `velocidade` e `marca`, e possui o método genérico `Mover`.

* **Carro**
  Herda de `Transporte` e implementa seu próprio método `Mover`.

* **Moto**
  Herda de `Transporte` e implementa seu próprio método `Mover`.

* **Bicicleta**
  Herda de `Transporte` e implementa seu próprio método `Mover`.

## Funcionamento

Ao instanciar cada classe e chamar o método `Mover`, cada objeto imprime sua própria mensagem personalizada.
O `super()` é utilizado para chamar o construtor da classe base e reaproveitar sua lógica de inicialização.

## Exemplo de Execução

```python
moto = Moto("120KM/h", "YAMAHA")
moto.Mover()

carro = Carro("140KM/h", "FERRARI")
carro.Mover()

bicicleta = Bicicleta("50KM", "KSW")
bicicleta.Mover()
```

## Saída esperada

```
A moto está acelerando
O carro está rodando pela estrada
A bicicleta está pedalando
```

---

Se quiser, posso melhorar o README com seções como requisitos, instalação ou explicações mais detalhadas.
