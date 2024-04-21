#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprima cada uma das palavras com as vogais duplicadas.

Ex:
python3 repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Carlos
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Caarloos
"""

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word: # condição de parada
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        # If comum
        if letter.lower() in "aeiouãêóíá":
            final_word += letter * 2
        else:
            final_word += letter
                
        # If Ternário
        #final_word += letter * 2 if letter.lower() in "aeiouãêóíá" else letter

    words.append(final_word)

    print(*words, sep="\n")