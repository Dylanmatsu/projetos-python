# =====================================================
# CALCULADORA DE RISCO DE INFARTO (Escore de Framingham)
# =====================================================


# ---------- FUNÇÃO PARA FAZER PERGUNTAS ----------
# Uma função é um "bloco pronto" que podemos usar várias vezes.
# Esta faz uma pergunta e só aceita respostas que estejam na lista de opções válidas.
def perguntar(texto, opcoes_validas):
    # input() mostra o texto e espera a pessoa digitar.
    # strip() tira espaços sobrando e lower() deixa tudo minúsculo ("F" vira "f").
    resposta = input(texto).strip().lower()

    # while = "enquanto". Repete a pergunta enquanto a resposta NÃO estiver nas opções válidas.
    while resposta not in opcoes_validas:
        resposta = input(texto).strip().lower()

    # Devolve a resposta válida para quem chamou a função.
    return resposta


# ---------- INÍCIO DO PROGRAMA ----------

# "pontos" guarda a soma da pontuação. Começa em zero.
pontos = 0

print("Calcule seu risco de infarto.")
print("Obs: Use o programa apenas se voce possui entre 30 e 74 anos.")

# ---------- 1) SEXO ----------
# Só aceita f ou m (maiúscula ou minúscula). Se digitar outra coisa, pergunta de novo.
sexo = perguntar("1) Qual seu sexo (F/M)? ", ["f", "m"])

# ---------- 2) IDADE ----------
# int() transforma o texto digitado em número inteiro.
idade = int(input("2) Qual sua idade? "))

# Se a idade for menor que 30 OU maior que 74, avisa e encerra o programa.
if idade < 30 or idade > 74:
    print("Idade invalida")
    exit()  # exit() termina o programa aqui

# Soma os pontos da idade. A tabela é diferente para homem e mulher.
if sexo == "m":
    if idade <= 34:
        pontos = pontos - 1
    elif idade <= 39:
        pontos = pontos + 0
    elif idade <= 44:
        pontos = pontos + 1
    elif idade <= 49:
        pontos = pontos + 2
    elif idade <= 54:
        pontos = pontos + 3
    elif idade <= 59:
        pontos = pontos + 4
    elif idade <= 64:
        pontos = pontos + 5
    elif idade <= 69:
        pontos = pontos + 6
    else:  # 70 a 74
        pontos = pontos + 7
else:  # mulher
    if idade <= 34:
        pontos = pontos - 9
    elif idade <= 39:
        pontos = pontos - 4
    elif idade <= 44:
        pontos = pontos + 0
    elif idade <= 49:
        pontos = pontos + 3
    elif idade <= 54:
        pontos = pontos + 6
    elif idade <= 59:
        pontos = pontos + 7
    else:  # 60 a 74
        pontos = pontos + 8

# ---------- 3) DIABETES ----------
# Só aceita s (sim) ou n (não).
diabetes = perguntar("3) Voce eh diabetico (S/N)? ", ["s", "n"])

if diabetes == "s":
    if sexo == "m":
        pontos = pontos + 2
    else:
        pontos = pontos + 4
# Se for "n" não soma nada (0 pontos), então não precisa de else.

# ---------- 4) FUMO ----------
fumante = perguntar("4) Voce eh fumante (S/N)? ", ["s", "n"])

if fumante == "s":
    pontos = pontos + 2  # fumar vale 2 pontos para homem e para mulher

# ---------- 5) COLESTEROL TOTAL ----------
print("5) Indique o seu colesterol total, usando a legenda:")
print("   a) <160")
print("   b) 160-199")
print("   c) 200-239")
print("   d) 240-279")
print("   e) >=280")
colesterol = perguntar("   ", ["a", "b", "c", "d", "e"])

if sexo == "m":
    if colesterol == "a":
        pontos = pontos - 3
    elif colesterol == "b":
        pontos = pontos + 0
    elif colesterol == "c":
        pontos = pontos + 1
    elif colesterol == "d":
        pontos = pontos + 2
    else:  # e
        pontos = pontos + 3
else:  # mulher
    if colesterol == "a":
        pontos = pontos - 2
    elif colesterol == "b":
        pontos = pontos + 0
    elif colesterol == "c":
        pontos = pontos + 1
    elif colesterol == "d":
        pontos = pontos + 1
    else:  # e
        pontos = pontos + 3

# ---------- 6) HDL COLESTEROL ----------
print("6) Indique o seu HDL colesterol, usando a legenda:")
print("   a) <35")
print("   b) 35-44")
print("   c) 45-49")
print("   d) 50-59")
print("   e) >=60")
hdl = perguntar("   ", ["a", "b", "c", "d", "e"])

if sexo == "m":
    if hdl == "a":
        pontos = pontos + 2
    elif hdl == "b":
        pontos = pontos + 1
    elif hdl == "c":
        pontos = pontos + 0
    elif hdl == "d":
        pontos = pontos + 0
    else:  # e
        pontos = pontos - 1
else:  # mulher
    if hdl == "a":
        pontos = pontos + 5
    elif hdl == "b":
        pontos = pontos + 2
    elif hdl == "c":
        pontos = pontos + 1
    elif hdl == "d":
        pontos = pontos + 0
    else:  # e
        pontos = pontos - 3

# ---------- 7) PRESSÃO ARTERIAL (PAS e PAD) ----------
print("7) Indique o seu PAS e PAD, usando a legenda:")
print("       PAS       PAD")
print("   a)  <120      <80")
print("   b)  120-129   80-84")
print("   c)  130-139   85-89")
print("   d)  140-159   90-99")
print("   e)  >=160     >=100")
pressao = perguntar("   ", ["a", "b", "c", "d", "e"])

if sexo == "m":
    if pressao == "a":
        pontos = pontos + 0
    elif pressao == "b":
        pontos = pontos + 0
    elif pressao == "c":
        pontos = pontos + 1
    elif pressao == "d":
        pontos = pontos + 2
    else:  # e
        pontos = pontos + 3
else:  # mulher
    if pressao == "a":
        pontos = pontos - 3
    elif pressao == "b":
        pontos = pontos + 0
    elif pressao == "c":
        pontos = pontos + 0
    elif pressao == "d":
        pontos = pontos + 2
    else:  # e
        pontos = pontos + 3

# ---------- CALCULANDO O RISCO ----------
# Cada lista abaixo é a linha "Risco em 10 anos" das tabelas do enunciado,
# na mesma ordem, da menor pontuação para a maior.
riscos_homem = [2, 3, 3, 4, 5, 7, 8, 10, 13, 16, 20, 25, 31, 37, 45, 53]
riscos_mulher = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10, 11, 13, 15, 18, 20, 24, 27]

# Precisamos transformar a pontuação em uma posição da lista (a posição começa em 0).
# Homem: pontuação -1 ou menos é a posição 0, então posição = pontos + 1
# Mulher: pontuação -2 ou menos é a posição 0, então posição = pontos + 2
if sexo == "m":
    posicao = pontos + 1
    ultima_posicao = 15  # última posição da lista de homens
else:
    posicao = pontos + 2
    ultima_posicao = 19  # última posição da lista de mulheres

# Se a pontuação for muito baixa ou muito alta, "prende" a posição dentro da lista.
if posicao < 0:
    posicao = 0
if posicao > ultima_posicao:
    posicao = ultima_posicao

# Pega o risco na posição certa da lista.
if sexo == "m":
    risco = riscos_homem[posicao]
else:
    risco = riscos_mulher[posicao]

# ---------- MOSTRANDO O RESULTADO ----------
print()
if posicao == ultima_posicao:
    # Na última posição da tabela o risco é "esse valor ou mais".
    print("Risco de infarto: pelo menos", str(risco) + "%")
else:
    print("Risco de infarto:", str(risco) + "%")

# Mensagem de acordo com o risco.
if risco <= 5:
    print("Excelente! Seu coracao esta em otima forma. Continue assim!")
elif risco <= 10:
    print("Muito bem! Risco baixo. Mantenha uma alimentacao equilibrada e se exercite.")
elif risco <= 20:
    print("Atencao! Risco moderado. Que tal uma caminhada hoje e uma visita ao medico?")
else:
    print("Alerta! Risco alto. Procure um medico o quanto antes e cuide do seu coracao!")