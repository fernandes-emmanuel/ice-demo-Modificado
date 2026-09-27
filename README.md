Before running, install the middleware and associated tools (on both machines):


## On Amazon Linux
```
sudo dnf install https://download.zeroc.com/ice/3.7/amzn2023/ice-repo-3.7.amzn2023.noarch.rpm
```

```
sudo dnf install python3-ice ice-compilers
```

## On Ubuntu
```
wget "https://download.zeroc.com/ice/3.8/ubuntu26.04/ice-repo-3.8_1.0.0_all.deb" -O ice-repo.deb
sudo dpkg -i ice-repo.deb
rm ice-repo.deb
sudo apt-get update
```
```
sudo apt-get install python3-zeroc-ice
```
```
sudo apt-get install zeroc-ice-compilers
```
Note: This code is exactly as in Example 3.21 of Maarten van Steen's book.

## Novos métodos

Além de `printString`, a interface `Printer` (arquivo `Printer.ice`) ganhou três novos métodos:

| Método | Descrição |
|---|---|
| `string printUpper(string s)` | Imprime o texto em letras maiúsculas no servidor e o retorna com um `*` no final |
| `int countWords(string s)` | Retorna a quantidade de palavras do texto |
| `int getPrintCount()` | Retorna quantas impressões aquele objeto já fez (cada objeto mantém seu próprio contador) |

Os servidores (`server.py` e `server2.py`) implementam os novos métodos, e os clientes (`client.py` e `client2.py`) chamam cada um deles e exibem as respostas.

Após alterar o `Printer.ice`, o código Python foi regenerado com:
```
slice2py Printer.ice
```

## Como executar

1. No servidor: `python3 server.py` (ou `python3 server2.py`)
2. No cliente, ajuste o IP do servidor no proxy em `client.py`/`client2.py` e execute `python3 client.py` (ou `python3 client2.py`)

Saída esperada do `client2.py`:
```
Hello World from printer1!*
Hello World from printer2!*
HELLO AGAIN FROM PRINTER1!*
7
2
1
```
