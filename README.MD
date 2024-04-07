twitter.com/rochacbruno

rochacbruno@gmail.com


## Shebang - define o interpretador do código
```python
#!/usr/bin/python3
#!/usr/bin/env python3
```

## Retorna o carminho do Python na máquina
```sh
which pyton3
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

## mostra onde está instalado seu python

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