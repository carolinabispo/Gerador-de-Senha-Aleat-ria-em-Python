﻿# Gerador-de-Senha-Aleatória-em-Python
Descrição do Projeto
Este projeto é um gerador de senhas aleatórias desenvolvido em Python. O objetivo é criar uma senha segura e única com base em um comprimento especificado pelo usuário. O código seleciona caracteres aleatórios de um conjunto de letras maiúsculas, minúsculas, números e símbolos especiais para formar uma senha.

# Funcionalidade
O programa solicita ao usuário que insira o comprimento desejado para a senha.
Em seguida, gera uma senha aleatória com esse comprimento, selecionando caracteres aleatórios de um conjunto predefinido que inclui letras, números e símbolos especiais.
A senha gerada é então exibida ao usuário.
Estrutura do Código
O código está dividido em três etapas principais:

# Definição do Conjunto de Caracteres Permitidos:

O conjunto de caracteres válidos para a senha é armazenado na lista caracteres_senha. Este conjunto inclui:
Letras maiúsculas: A-Z
Letras minúsculas: a-z
Símbolos especiais: !@#$%^&*()-_=+
Números: 0-9
Entrada do Usuário:

O programa solicita que o usuário forneça o comprimento desejado para a senha através da função input().
O valor informado é convertido para um número inteiro utilizando int().
Geração da Senha:

O programa usa um loop for para gerar a senha. Para cada iteração, a função random.choice() é utilizada para escolher um caractere aleatório da lista caracteres_senha.
O caractere sorteado é adicionado à lista caracteres_inclusos.
Após o loop, os caracteres na lista caracteres_inclusos são unidos em uma string com o método ''.join() e a senha gerada é exibida ao usuário.
