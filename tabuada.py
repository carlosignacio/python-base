#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

    1 x 1 = 1
    2 x 2 = 2
    3 x 1 = 3
...
###################
---Tabuada do 2---

    2 x 1 = 2
    2 x 2 = 4
...
###################
"""
__version__ = "0.1.1"
__author__ = "Carlos"

# template = """
# ---Tabuada do 1---

# {bloco:^18}


# ###################
# """

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

# Itarable (percorriveis)

# para
for n1 in numeros:
    #bloco = ""
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
        #bloco += f"{n1} x {n2} = {resultado}\n"
        #print(operacao)
    #print(template.format(bloco=bloco))
    print("#" * 18)
    