twitter.com/rochacbruno

rochacbruno@gmail.com

## Python Tutor (Por ser utilizado para debbug simples)
Exercicio da tabuada por ser utilizado no teste dessa ferramenta

https://pythontutor.com/

>Start coding online now in **Python**

# Lista 
* [ ]

# Tupla
* ( )

# Dicionário
* { }

## Statement

>**_"Statement"_** são as palavras de ordem do Python, que checam alguma coisa, não retornam valor, mas verificam algo.

* Se        -> if
* Senão, se -> elif
* Senão,    -> else
* E         -> and
* OU        -> or
* Não       -> not

## Assignment

* Perguntas..

Exemplo:

A padaria está aberta?

## Expressões

>**_"Expressão"_** é a junção entre as conexões lógicas e condições que avaliam para booleano. Toda vez que eu esperar uma resposta, consideramos uma expressão.

Exemplo:

É feriado? (True or False)

## Actions

* Função
* Método
* Instrução


## Testes arquivo hello.py

```sh
python3 hello.py --lang=pt_BR
```

## Testes arquivo prefixcalc.py

```sh
python3 prefixcalc.py sum 9 1
```

## Testes arquivo notes.py

```sh
python3 notes.py new "Minha terceira Nota"
```

## Pesquisar palavras no codigo fonte do git

```sh
git grep "TODO:"
```


## Shebang - define o interpretador do código
```python
#!/usr/bin/python3
#!/usr/bin/env python3
```

## Retorna o carminho do Python na máquina
```sh
which python3
```

## Ver usuário
```sh
whoami
```

## Permissão de execução
```sh
chmod +x hello.py
```

## Guia de estilo do python

```
pep8.org
````
```
Boa prática até 80 colunas e o recomendado é chegar na 79 e quebrar para a linha seguinte
```
### Dunder é o mesmo que __ (2 underlines) (Double underlines)

```sh
_
```

## Snake case = Ocorre quando as palavras são todas em minúsculo e separadas por underline
current_language

## Pascal Case = Ocorre quando as palavras são Juntas e cada uma inicia com Maiúsculo
CurrentLanguage

## Módulo "site" mostra qual é o ambiente do python.
#### Mostra onde está localizado os arquivos, os pacotes e o interpretador python

```sh
python3 -m site
```

## Mostra onde está instalado seu python

```sh
which python
```

## Cria o ambiente virtual python com o nome ".venv"

```sh
python3 -m venv .venv
```

## Ativando o ambiente virtual do python (Comando linux)

```sh
source .venv/bin/activate
```

## Utilizando pip "https://pypi.org" para instalar o ipython (mesmo que o Jupyter online)

```sh
python3 -m pip install ipython
```

#### help no ipython

>help("synbols")
>help("**")

## Upgrade pip

```sh
python3 -m pip install --upgrade pip
```

## concatenação (usado em logging)

```python
%s
```

## str.format (Usado em mensagens longas, e-mail)

```python
{}
```
## f-strings (restante, msg, print, error)

```python
f"olá, {nome}"
```

## Imprimir itens de uma lista em uma nova linha e de forma limpa utilizando DESEMPACOTAMENTO (*)
```python

nomes = ["Carlos", "Miria", "Eduardo"]

# Desempacotamento (*) com separador com quebra de linha
print(*nomes, sep="\n")
```

## Elipses
... > Elipses (reticencias)

Significa que a lista continua

## placeholder

```python
{}
```
https://replit.com/@rochacbruno/LTBASEESCOLACLEAN#main.py

## Type set
```
Coleção desordenada (sem garantia) porém única. Normalmente alfa-númérica
Objetos de 
Utiliza Hash Table

set = conjuntos 
{} ou set()

União =                 |   ou    .union
Interseção =            &   ou    .insersection
Diferença =             -   ou    .difference
Diferença simétrica =   ^   ou    .symemtric_difference
```

## Dicionário
```
key - > value
{key:value}
{"nome": "Bruno", "cod": 123}
    [0],             [1]
 {key:value, key:value}
```
## Utilizando comando print para criar arquivo e escrever dentro
```python
print("parece mágica", file=open("hello.txt", "a"))

print("Hello", file=open("hello.txt", "a"))

print("Cada Linha", file=open("hello.txt", "a"))
```

## Removendo espaços em branco do começo e do final
```python
.strip()
```

Exemplo:

```python
nome = input("Qual o seu nome").strip()
```

## Acessar as variáveis de ambiente

```python
import os
os.getenv
```

Exemplo:

```python
import os

current_language = os.getenv("LANG", "en_US")[:5]
```

## Debugging

Exemplo:

```python
import.sys

print(f"Banana - {sys.argv=}")

sys.argv=['/Users/carlo.ignacio/pdi/linuxtips-python/python-base/hello.py', '--lang=fr_FR']
```

## Imprimindo argumentos

Exemplo:

```sh
python3 hello.py --lang=fr_FR --count=5
```

## Removendo caracteres da esquerda para a direita

```python
.lstrip("-")
```

## Criar pasta ignorando erro no comando se a pasta existir

```python
import os

os.makedirs("pasta1/subpasta", exist_ok=True)

# Boa prática para criar pastas independente do Sistema Operacional

path = os.path.join("pasta", "subpasta")

os.makedirs(path, exist_ok=True)

```

## File Descriptor

```python
import os

# caminho direto para o arquivo
filepath = os.path.join(path, "arquivo.txt")

# por padrão ele abre em modo leitura
open(filepath)

arquivo = open(filepath)

# Abrindo o arquivo em modo escrita 
# Ao abrir o arquivo com o "W", ele sempre substitui o 
# conteúdo do arquivo
open(filepath, "w")

arquivo = open(filepath, "w")
arquivo.write("Carlos\n")
arquivo.write("Eduardo\n")
arquivo.write("Ignácio\n")
arquivo.,close()

print(open(filepath).read())

# Abrindo o arquivo em modo escrita (append),
# Adicionando o arquivo na próxima linha

arquivo = open(filepath, "a")
arquivo.write("Eduardo\n")
arquivo.write("Ignácio\n")
arquivo.,close()

print(open(filepath).read())
```

## Context Manager
####

**with** - Escrever em um arquivo sem precisar do close

```python
import os

filepath = os.path.join(path, "arquivo.txt")

with open(filepath, "a") as arquivo:
    arquivo.write("Hello\n")
    arquivo.write("World\n")

open(filepath).read()

print("Brasil", file=open(filepath, "a"))
```

## pathlib

```python
import os
from pathlib import Path

# criando pasta
Path("pasta")

# criando pasta e subpasta
Path("pasta") / Path("subpasta")

path = Path("pasta") / Path("subpasta")

# criando o arquivo no path
path / Path("novo.txt")

filepath = path / Path("novo.txt")

```

## Datetime

```python
from datetime import datetime

# imprime a data e a hora atual 
datetime.now()

# imprime formato para usar em timestamp
datetime.now().isoformat()

```

## LYBL - Look Before You Leap

```python
#!/usr/bin/env python3

import os
import sys

# LYBL - Look Before You Leap

if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[1])
else: 
    print("[Error]: Missing name in the list")
    sys.exit(1)
```

## Race Condiction

```python
#!/usr/bin/env python3

import os
import sys

# LYBL - Look Before You Leap

if os.path.exists("names.txt"):
    print('O arquivo existe')
    input("...") # Race Condiction
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[1])
else: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

## EAFP - Easy for ASK Forgiveness than permission
### (É mais fácil pedir perdão do que permissão)

Exemplo 1:

```python
#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()
except:
    print("[Error] File names.txt not found.")
    sys.exit(1)

try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

#### Bare except

Exemplo 2:

```python
#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()
except: # Bare except
    print("[Error] File names.txt not found.")
    sys.exit(1)

try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

Exemplo 3:

```python
#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines() # FileNotFoundError
    #1 / 0 # ZeroDivisionError
    1 / 1 
    #print(names.banana) # AttributeError
    print(names.append)
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You can't divide by zero")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn`t have banana")    
    sys.exit(1)
try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

Exemplo 4:

```python
#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines() 
    # FileNotFoundError
    print(names.append)
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre")

try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

Exemplo 5

```python
#!/usr/bin/env python3

import os
import sys

# EAFP - Easy for ASK Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines() 
    # FileNotFoundError
    print(names.append)
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre")

try:
    print(names[1])
except: 
    print("[Error]: Missing name in the list")
    sys.exit(1)

```

## Logs de Erro de Execução utlizando LOGGING

Apresenta o erro no momento que ele acontece

<https://docs.python.org/3/library/logging.html=logging-levels>

Exemplo 1:

```python
#!/usr/bin/env python3
"""
"""
import os
import logging

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instancia
log = logging.Logger("logs.py", log_level)
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(logging.DEBUG)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

log.critical("Erro geral ex: banco de dados sumiu")
log.debug("Mensagem pro dev, qa, sysadmin")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.info("Mensagem geral para usuarios")

print("---")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))
    # stdout
    # sterr
```

## Condição Ternária (If ternário ou if inline)

Ao utilizar o Ternário, é obrigatório utilizar o "else", para definir o valor default, caso a condição não seja "True"

```python
n1 = 1
n2 = 9
nome = "Carlos"


# Esse fornato TRADICIONAL
if n2 > n1:
    valor = "ok"

# Pode ser feito na forma TERNÁRIA - Exemplo 1
valor = "ok" if n2 > n1 else "nok"

# Pode ser feito na forma TERNÁRIA - Exemplo 2
print("ok" if n2 < n1 else "nok")

# Esse fornato TRADICIONAL
if nome != "":
    nome = "pessoa"

# Pode ser feito na forma TERNÁRIA - Exemplo 3
print(f"Ola {nome or 'pessoa'}, boas vindas.")
```

## Iteração com FOR

Exemplo 1 - "Range"

```python
#!/usr/bin/env python3

#### Gera uma lista de número do 1 até o 699, pulando de 2 em 2
numbers = range(1, 700, 2) # start, next, stop, step

# Iterable
for number in numbers:
    print(number)
```

Exemplo 2 - "Continue"

```python
#!/usr/bin/env python3
"""
"""
#numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1,11)

#### Imprime apenas número pares
# Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue # Reinicia o processo para o for, até o final dos números
    
    print(f"mais codigo com {number}")
```

Exemplo 3 - "Break"

```python
#!/usr/bin/env python3
"""
"""
#numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1,11)

#### Imprime apenas número pares
# Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        break # Interrompe o processo mesmo que tenham ações a fazer
    
    print(f"mais codigo com {number}")
```

Exemplo 4 - "Ler conteúdo de um Arquivo de texto e imprimir as linhas do arquivo"

- Criar arquivo "post.txt"
```
title: Meu post
tags:tech,geral
date:2022-02-10
published:1
---
Este é o meu post
Aqui tem texto e conteudo
etc. etc. etc.
```

```python
#!/usr/bin/env python3

# Abre o arquivo e imprime as linhas
for line in open("post.txt"):
    print(line)
```

Exemplo 5 - "Ler conteúdo de um Arquivo de texto e imprimir as linhas do arquivo até encontrar a linha com '---\n' sendo o \n uma quebra de linha"

- Criar arquivo "post.txt"
```
title: Meu post
tags:tech,geral
date:2022-02-10
published:1
---
Este é o meu post
Aqui tem texto e conteudo
etc. etc. etc.
```

```python
#!/usr/bin/env python3

# Abre o arquivo e imprime as linhas até encontrar o "---\n"
for line in open("post.txt"):
    if line == "---\n":
        break
    print(line)
```

Exemplo 6 - "Ler conteúdo de um Arquivo de texto e imprimir as linhas do arquivo até encontrar a linha com '---\n' sendo o \n uma quebra de linha e criar um dicionário com o conteúdo"

- Criar arquivo "post.txt"
```
title: Meu post
tags:tech,geral
date:2022-02-10
published:1
---
Este é o meu post
Aqui tem texto e conteudo
etc. etc. etc.
```

```python
#!/usr/bin/env python3

dados = {}
for line in open("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip() # strip remove caracteres especiais, nesse caso removeu o \n
    
print(dados)
```

Exemplo 7 -  For loops / Laço for

- Criando uma nova Lista

```python
#!/usr/bin/env python3

original = [1, 2, 3]
dobrada = []
for n in original:
    dobrada.append(n * 2)

print(dobrada)
```

Exemplo 8 -  List Comprehension (Funcional)

- Criando uma nova Lista

```python
#!/usr/bin/env python3

# For loops / Laço for
original = [1, 2, 3]
dobrada = []
for n in original:
    dobrada.append(n * 2)

print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)
```

Exemplo 9 -  Dict Comprehension

- Criando uma nova Lista

```python
#!/usr/bin/env python3

# Abre o arquivo e imprime as linhas
for line in open("post.txt"):
    print(line)

# Abre o arquivo e imprime as linhas em um dicionário
dados = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)

# Dict comprehension
dados = {line for line in open("post.txt") if ":" in line}
print(dados)

# Dict comprehension utilizando "Dicionario direto"
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt") 
    if ":" in line
}
print(dados)
```

## While - Enquanto

Repetir algo até que a condição seja verdadeira (True).

Exemplo 1 - "Loop infinit, main loop"

```python
#!/usr/bin/env python3

n = 0
while True: # loop infinito, main loop
    print(n)
    n += 1
```

Exemplo 2 - Condição de parada

- "Imprimir até o 100"

```python
#!/usr/bin/env python3

n = 0
while n < 101:
    print(n)
    n += 1
```

Exemplo 3 - Condição de parada (Break)

- "Imprimir até o 39"

```python
#!/usr/bin/env python3

n = 0
while n < 101:
    if n == 40:
        break
    print(n)
    n += 1
```

Exemplo 4 - Condição de continue 

- "Imprimir pulando o 40"

```python
#!/usr/bin/env python3

n = 0
while n < 101:
    if n == 40:
        n += 1        
        continue
    print(n)
    n += 1
```

Exemplo 5 - Condição de continue 

- "Imprimir pulando do 40 ao 60"

```python
#!/usr/bin/env python3

n = 0
while n < 101:
    if n >= 40 and  n<= 60:
        n += 1        
        continue
    print(n)
    n += 1
```

Exemplo 5 - Condição de continue 

- "Imprimir apenas números pares"

```python
#!/usr/bin/env python3

n = 0
while n < 101:
    if n % 2 != 0:
        n += 1        
        continue
    print(n)
    n += 1
```

Exemplo 6 
- "Refatorando notes.py"

```python
#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path =  os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

while True:

    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()

        # leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o título:").strip().title()

        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")

    cont = input(f"Quer continuar {arguments[0]} notas? [N/y]").strip().lower()
    if cont != "y":
        break
```

Exemplo 7 
- "Refatorando prefixcalc.py"

```python
#!/usr/bin/env python3
"""Calculadora prefix.

Funcionamento:

[operacao] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operacao: sum
n1: 5
n2: 4
9

Os Resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.0"

import os
import sys

from datetime import datetime



while True:

    arguments = sys.argv[1:]
    
    # Validação
    if not arguments:
        operation = input("Operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("Ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation  not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        # TODO: Repetição com while + exceptions
        if not num.replace(".", "").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    # TODO: Usar dict de funcoes
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2       
    elif operation == "div":
        result = n1 / n2

    print(f"O resultado é {result}")

    path = os.curdir
    filepath = os.path.join(path, "prefixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except PermissionError as e:
        # TODO: logging
        print(str(e))
        sys.exit(1)

    if input("Pressione enter para continuar ou qualquer tecla para sair"):
        break
```