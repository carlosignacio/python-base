#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista de quartos disponíveis para alugar e o preço de cada quarto, 
esta informação está disponível em um arquivo de texto separado por vírgulas.

'quartos.txt'
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
4,Quarto Single,100
5,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado, a quantidade de dias e no final exibe
o valor estimado a ser pago

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reservas.txt'
# cliente, quarto, dias
Carlos,3,12

Se o outro usuário tentar reservar o mesmo quarto o programa deve exibir uma mensagem informando que já está reservado.
"""
import sys
import logging

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# Acesso ao banco de dados
ocupados = {} # acumulador
try:
    for line in open(RESERVAS_FILE):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": int(dias)
        }
except FileNotFoundError:
    logging.error("Arquivo %S não existe", RESERVAS_FILE)
    sys.exit(1)

# TODO: Usar função para ler os arquivos

quartos = {} # acumulador
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)

# Programa Principal
print("Reservas no Hotel Pythonico da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel está lotado, volte depois.")
    sys.exit(0)

nome = input("Qual é o seu nome:").strip()
print()
print("Lista de quartos:")
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "❌" if not dados_quarto['disponivel']  else "✅"
    #disponivel = dados['disponivel'] and "✅" or "❌"
    # TODO: Substituir casa decimal por vírgula
    print(f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<9.2f} - {disponivel:<10}")


print("-" * 52)
# reserva
try:
    num_quarto = int(input("Qual o quarto desejado:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro.")
        sys.exit(0)
except ValueError:
    logging.error("Número inválido, digite apenas dígitos.")
    sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)
try:
    dias = int(input("Quantos dias?:").strip())
except ValueError:
    logging.error("Número inválido, digite apenas dígitos.")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
#disponivel = quartos[num_quarto]["disponivel"]
total = preco_diaria * dias

# print(",").join([nome, str(num_quarto), str(dias)])

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")

if input("Confirma? (digite y) ").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome},{num_quarto},{dias}\n")
