import random
from os import system, name

# Função para limpar a tela
def limpa_tela():
    # Windows
    if name == "nt":
        _ = system("cls")
    # Linux/Mac
    else:
        _ = system("clear")

def game():
    limpa_tela()

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'laranja', 'morango']

    #escolhe de forma random uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descorbertas = ['_' for letra in palavra]

    #numero de chances
    chances = 6

    #lista para letras erradas
    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descorbertas))
        print(f"\nchances restantes: {chances}")
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\ninsira uma letra: ").lower()

        if tentativa in palavra:
            index = 0 
            for letra in palavra:
                if tentativa == letra:
                    letras_descorbertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descorbertas:
            print(f"\nvocê venceu! a palavras era: {palavra}")
            break
    
    if "_" in letras_descorbertas:
        print(f"voce perdeu, a palavra era: {palavra}")

#bloco main

if __name__ == "__main__":
    game()
    print("\n parabens eu estou aprendendo programação em python")


