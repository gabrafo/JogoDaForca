import random

palavrasLista = ["PYTHON", "PROGRAMAÇÃO", "JAVA", "JAVASCRIPT", "VSCODE", "INTELLIJ", "BLUEJ", "RUBY", "COMPUTAÇÃO", "DESENVOLVIMENTO", "TECNOLOGIA",
                 "CIÊNCIA", "ASSEMBLY", "CYBERSEC", "LINGUAGEM"]
palavraSecreta = random.choice(palavrasLista)
underline = "_" * len(palavraSecreta)  # Cria uma string de underlines com o mesmo comprimento da palavraSecreta
forcaExibicao = ["""
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========
""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
========
""", """
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
========
""", """
   +---+
   |   |
   O   |
   |   |
  /    |
       |
========
""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
========
""", """
   +---+
   |   |
   O   |
       |
       |
       |
========
""", """
   +---+
   |   |
       |
       |
       |
       |
========
"""]
# Uso de aspas múltiplas p/ Strings multilinhas

letra = ""
erros = []  # Lista vazia, comentário em Python
chances = 6
print("Você terá", chances+1, "chances.")

# Laço For em Python -> for elemento in range(NúmeroDeExecuções):
# For Each em Python -> for elemento in coleção:

print("A palavra tem:", len(palavraSecreta), "letras.")

print(forcaExibicao[6])

keepPlaying = True # Tem que ter letra maiúscula

while keepPlaying and chances>0:
    print(underline, "\n")
    letra = input("Insira uma letra: ").upper() # Deixa a letra automaticamente maiúscula

    while len(letra) != 1 or not letra.isalpha():
        # Checa se a entrada é apenas um caractér e se esse caractér é uma letra do alfabeto
        print("Por favor, insira apenas uma letra válida.")
        letra = input("Insira uma letra: ").upper()  # Deixa a letra automaticamente maiúscula

    while letra in erros:
        print("Letra inválida.\n")
        letra = input("Insira uma letra: ").upper()  # Deixa a letra automaticamente maiúscula

    if letra in palavraSecreta:
        for i in range(len(palavraSecreta)):
            if letra == palavraSecreta[i]:
                underline = underline[:i] + letra + underline[i+1:] # Mantém a String, mudando apenas as letras encontradas

        print("Letra correta!")

    else:
        print("Letra não encontrada.")
        erros.append(letra)
        chances -= 1
        print(forcaExibicao[chances])

    if chances==0:
        print("Você perdeu! A palavra era:", palavraSecreta)
        keepPlaying = False

    if "_" not in underline:
        print(underline, "\n")
        print("Você venceu! Parabéns!")
        keepPlaying = False
