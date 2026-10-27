##################################################
# Urna Eletrônica (Python)                       #
# Projeto da faculdade - Ciência da Computação   #
# Feito em dupla                                 #
##################################################

# ------------------------------------------------------------
# 1.1) ABRIR A URNA ELETRÔNICA
# ------------------------------------------------------------
# print() mostra um texto na tela
print("=" * 50)
print("IDENTIFICAÇÃO DA URNA ELETRÔNICA")
print("=" * 50)

# input() pergunta algo ao usuário e guarda a resposta em uma variável
zona = input("Número da Zona Eleitoral..............: ")
secao = input("Número da Seção Eleitoral..............: ")
codigo_urna = input("Código de Identificação da Urna.......: ")

# int() transforma o texto digitado em número inteiro (para poder fazer contas)
total_esperado = int(input("Total de eleitores que podem votar....: "))

# ------------------------------------------------------------
# VARIÁVEIS CONTADORAS (todas começam em zero)
# ------------------------------------------------------------
# Cada uma guarda quantos votos aquele candidato recebeu

# Prefeito
c1 = 0
c2 = 0
c3 = 0
c4 = 0
brancos_prefeito = 0
nulos_prefeito = 0

# Vereador
v1 = 0
v2 = 0
v3 = 0
v4 = 0
brancos_vereador = 0
nulos_vereador = 0

# Conta quantos eleitores já votaram
votaram = 0

# ------------------------------------------------------------
# 1.2) RECEBER OS VOTOS
# ------------------------------------------------------------
print()
print("VOTAÇÃO INDIVIDUAL")
print("Candidatos a Prefeito: C1, C2, C3, C4 | Branco: VB | Nulo: VN")
print("Candidatos a Vereador: V1, V2, V3, V4 | Branco: VB | Nulo: VN")
print("Para ENCERRAR a votação antes do fim, digite: FIM")

# while repete o bloco de baixo enquanto a condição for verdadeira.
# Aqui: repete enquanto ainda faltam eleitores para votar.
while votaram < total_esperado:

    print()
    # votaram + 1 é o número do eleitor da vez (o primeiro é o 1)
    print("Eleitor", votaram + 1)

    # .strip() tira espaços extras e .upper() deixa tudo maiúsculo
    # (assim "c1" e "C1" valem a mesma coisa)
    voto_prefeito = input(" Voto ao Candidato à Prefeitura..: ").strip().upper()

    # Se digitou FIM, o break sai do while na hora (votação encerrada)
    if voto_prefeito == "FIM":
        break

    voto_vereador = input(" Voto ao Candidato a Vereador....: ").strip().upper()

    if voto_vereador == "FIM":
        break

    # ----- Confere o voto para Prefeito -----
    # if / elif / else: testa uma opção por vez, na ordem
    if voto_prefeito == "C1":
        c1 = c1 + 1          # soma 1 voto para o C1
    elif voto_prefeito == "C2":
        c2 = c2 + 1
    elif voto_prefeito == "C3":
        c3 = c3 + 1
    elif voto_prefeito == "C4":
        c4 = c4 + 1
    elif voto_prefeito == "VB":
        brancos_prefeito = brancos_prefeito + 1
    else:
        # Qualquer outra coisa digitada (VN ou erro) conta como voto nulo
        nulos_prefeito = nulos_prefeito + 1

    # ----- Confere o voto para Vereador -----
    if voto_vereador == "V1":
        v1 = v1 + 1
    elif voto_vereador == "V2":
        v2 = v2 + 1
    elif voto_vereador == "V3":
        v3 = v3 + 1
    elif voto_vereador == "V4":
        v4 = v4 + 1
    elif voto_vereador == "VB":
        brancos_vereador = brancos_vereador + 1
    else:
        nulos_vereador = nulos_vereador + 1

    # Este eleitor terminou de votar, então soma 1 em quem já votou
    votaram = votaram + 1

print()
print("ENCERRAMENTO DAS ELEIÇÕES")

# ------------------------------------------------------------
# 2) TOTALIZAÇÃO (fazendo as contas finais)
# ------------------------------------------------------------
# Quem não votou é quem podia votar menos quem votou
faltaram = total_esperado - votaram

# Votos do partido = soma dos votos dos candidatos dele
# PDB tem os candidatos 1 e 2 | PSB tem os candidatos 3 e 4
pdb_prefeito = c1 + c2
psb_prefeito = c3 + c4
pdb_vereador = v1 + v2
psb_vereador = v3 + v4

# Total de votos válidos (só de candidatos, sem branco e nulo)
apurados_prefeito = c1 + c2 + c3 + c4
apurados_vereador = v1 + v2 + v3 + v4

# Descobrir o Prefeito mais votado:
# começamos achando que o C1 é o mais votado e vamos comparando com os outros
maior_prefeito = c1
nome_prefeito = "C1"
if c2 > maior_prefeito:
    maior_prefeito = c2
    nome_prefeito = "C2"
if c3 > maior_prefeito:
    maior_prefeito = c3
    nome_prefeito = "C3"
if c4 > maior_prefeito:
    maior_prefeito = c4
    nome_prefeito = "C4"

# Se ninguém recebeu voto, não existe "mais votado"
# (em caso de empate, mostra o primeiro da lista)
if maior_prefeito == 0:
    nome_prefeito = "Nenhum (sem votos)"

# Mesma ideia para o Vereador mais votado
maior_vereador = v1
nome_vereador = "V1"
if v2 > maior_vereador:
    maior_vereador = v2
    nome_vereador = "V2"
if v3 > maior_vereador:
    maior_vereador = v3
    nome_vereador = "V3"
if v4 > maior_vereador:
    maior_vereador = v4
    nome_vereador = "V4"

if maior_vereador == 0:
    nome_vereador = "Nenhum (sem votos)"

# ------------------------------------------------------------
# 3) DIVULGAÇÃO DOS RESULTADOS
# ------------------------------------------------------------
print()
print("=" * 50)
print("RESULTADO DA ELEIÇÃO")
print("=" * 50)
print("Zona Eleitoral...................:", zona)
print("Seção Eleitoral..................:", secao)
print("Código da Urna Eletrônica........:", codigo_urna)
print("Eleitores que podem votar........:", total_esperado)
print("Eleitores que votaram............:", votaram)
print("Eleitores que faltaram...........:", faltaram)

print()
print("----- PREFEITO -----")
print("Número de votos para o Partido PDB:", pdb_prefeito)
print("Número de votos para o Partido PSB:", psb_prefeito)
print("Número de votos para o Candidato C1:", c1)
print("Número de votos para o Candidato C2:", c2)
print("Número de votos para o Candidato C3:", c3)
print("Número de votos para o Candidato C4:", c4)
print("Número de votos brancos:", brancos_prefeito)
print("Número de votos nulos:", nulos_prefeito)
print("Total de votos apurados:", apurados_prefeito)
print("Candidato a Prefeito mais votado:", nome_prefeito)

print()
print("----- VEREADOR -----")
print("Número de votos para o Partido PDB:", pdb_vereador)
print("Número de votos para o Partido PSB:", psb_vereador)
print("Número de votos para o Candidato V1:", v1)
print("Número de votos para o Candidato V2:", v2)
print("Número de votos para o Candidato V3:", v3)
print("Número de votos para o Candidato V4:", v4)
print("Número de votos brancos:", brancos_vereador)
print("Número de votos nulos:", nulos_vereador)
print("Total de votos apurados:", apurados_vereador)
print("Candidato a Vereador mais votado:", nome_vereador)
