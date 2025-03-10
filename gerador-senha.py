import random

caracteres_senha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


comprimeto_senha_usuario = int(input(f"Por favor, insira o comprimento de senha desejada:"))

caracteres_inclusos = []

for i in range(comprimeto_senha_usuario):
    sorteio = random.choice(caracteres_senha)
   
    caracteres_inclusos.append(sorteio)
print(f"Senha gerada:","".join(caracteres_inclusos))
    
