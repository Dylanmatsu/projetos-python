##################################################
# 4º Projeto - Funções (Divisibilidade)          #
# Aluno: Dylan Matsumoto Ishibashi               #
##################################################
# TURMA: CC2P33                                  #
# Disciplina: Projeto e Desenvolvimento de       #
#             Algoritmos II                      #
# Profa. Eliane                                  #
##################################################
# Objetivo: dizer se um número (dividendo) é divisível por
#           outro (divisor) usando as REGRAS de divisibilidade,
#           sem usar "numero % divisor == 0".
##################################################


# ---------- Mensagem inicial ----------
def imprimirObjetivoLab():
    # Só mostra o texto de apresentação na tela
    print("Programa TESTE DE DIVISIBILIDADE")
    print()
    print("O programa tem por objetivo informar se um determinado")
    print("numero eh ou nao divisivel por outro.")
    print()
    print("Os testes de divisibilidade sao validos para os seguintes")
    print("divisores: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15 e 25.")


# ---------- Divisível por 2 ----------
def divisibilidade2(num):
    # Regra: é divisível por 2 se o último algarismo for 0, 2, 4, 6 ou 8
    ultimo = num % 10  # pega o último algarismo (permitido pela Dica 1)
    resultado = (ultimo == 0 or ultimo == 2 or ultimo == 4
                 or ultimo == 6 or ultimo == 8)
    return resultado  # único return da função


# ---------- Divisível por 3 ----------
def divisibilidade3(num):
    # Regra: soma os algarismos; repete até sobrar 1 dígito.
    # Se esse dígito for 3, 6 ou 9, o número é divisível por 3.
    while num >= 10:           # repete enquanto tiver mais de 1 dígito
        soma = 0
        while num > 0:
            soma = soma + num % 10   # soma o último algarismo
            num = num // 10          # tira o último algarismo
        num = soma                   # a soma vira o novo número
    resultado = (num == 3 or num == 6 or num == 9)
    return resultado


# ---------- Divisível por 4 ----------
def divisibilidade4(num):
    # Regra: divisível duas vezes por 2
    resultado = False
    if divisibilidade2(num):            # 1ª vez por 2
        metade = num // 2
        if divisibilidade2(metade):     # 2ª vez por 2
            resultado = True
    return resultado


# ---------- Divisível por 5 ----------
def divisibilidade5(num):
    # Regra: termina em 0 ou 5
    ultimo = num % 10
    resultado = (ultimo == 0 or ultimo == 5)
    return resultado


# ---------- Divisível por 6 ----------
def divisibilidade6(num):
    # Regra: divisível por 2 e por 3 ao mesmo tempo
    resultado = divisibilidade2(num) and divisibilidade3(num)
    return resultado


# ---------- Divisível por 7 ----------
def divisibilidade7(num):
    # Regra: pega o último algarismo, multiplica por 2 e subtrai
    # do resto do número. Repete até o resultado ser <= 70.
    # No fim, confere se está na tabuada do 7.
    while num > 70:
        ultimo = num % 10          # último algarismo
        resto = num // 10          # número sem o último algarismo
        num = abs(resto - ultimo * 2)   # abs = valor sem sinal (módulo)
    # tabuada do 7 até 70
    resultado = (num == 0 or num == 7 or num == 14 or num == 21
                 or num == 28 or num == 35 or num == 42 or num == 49
                 or num == 56 or num == 63 or num == 70)
    return resultado


# ---------- Divisível por 8 ----------
def divisibilidade8(num):
    # Regra: divisível três vezes por 2
    resultado = False
    if divisibilidade2(num):                # 1ª vez
        metade = num // 2
        if divisibilidade2(metade):         # 2ª vez
            quarto = metade // 2
            if divisibilidade2(quarto):     # 3ª vez
                resultado = True
    return resultado


# ---------- Divisível por 9 ----------
def divisibilidade9(num):
    # Regra: divisível duas vezes por 3
    resultado = False
    if divisibilidade3(num):            # 1ª vez por 3
        terco = num // 3
        if divisibilidade3(terco):      # 2ª vez por 3
            resultado = True
    return resultado


# ---------- Divisível por 10 ----------
def divisibilidade10(num):
    # Regra: termina em 0
    ultimo = num % 10
    resultado = (ultimo == 0)
    return resultado


# ---------- Divisível por 11 ----------
def divisibilidade11(num):
    # Regra: soma os algarismos de posição ímpar (Si) e de posição par (Sp),
    # contando da direita para a esquerda (o último é o 1º, ímpar).
    # Calcula |Si - Sp| e repete até sobrar 1 dígito. Se for 0, é divisível.
    while num >= 10:
        si = 0            # soma dos algarismos de ordem ímpar
        sp = 0            # soma dos algarismos de ordem par
        ordem_impar = True    # True = posição ímpar, False = posição par
                              # (começa True: o último algarismo é o 1º, ímpar)
        while num > 0:
            ultimo = num % 10         # algarismo atual
            if ordem_impar:           # posição ímpar
                si = si + ultimo
            else:                     # posição par
                sp = sp + ultimo
            num = num // 10           # tira o algarismo
            ordem_impar = not ordem_impar   # alterna: ímpar <-> par
        num = abs(si - sp)            # diferença sem sinal
    resultado = (num == 0)
    return resultado


# ---------- Divisível por 12 ----------
def divisibilidade12(num):
    # Regra: divisível por 3 e por 4
    resultado = divisibilidade3(num) and divisibilidade4(num)
    return resultado


# ---------- Divisível por 15 ----------
def divisibilidade15(num):
    # Regra: divisível por 3 e por 5
    resultado = divisibilidade3(num) and divisibilidade5(num)
    return resultado


# ---------- Divisível por 25 ----------
def divisibilidade25(num):
    # Regra: divisível duas vezes por 5
    resultado = False
    if divisibilidade5(num):            # 1ª vez por 5
        quinto = num // 5
        if divisibilidade5(quinto):     # 2ª vez por 5
            resultado = True
    return resultado


# ---------- Escolhe qual regra usar ----------
def testarDivisibilidade(dividendo, divisor):
    # Olha o divisor e chama a função certa
    if divisor == 2:
        resultado = divisibilidade2(dividendo)
    elif divisor == 3:
        resultado = divisibilidade3(dividendo)
    elif divisor == 4:
        resultado = divisibilidade4(dividendo)
    elif divisor == 5:
        resultado = divisibilidade5(dividendo)
    elif divisor == 6:
        resultado = divisibilidade6(dividendo)
    elif divisor == 7:
        resultado = divisibilidade7(dividendo)
    elif divisor == 8:
        resultado = divisibilidade8(dividendo)
    elif divisor == 9:
        resultado = divisibilidade9(dividendo)
    elif divisor == 10:
        resultado = divisibilidade10(dividendo)
    elif divisor == 11:
        resultado = divisibilidade11(dividendo)
    elif divisor == 12:
        resultado = divisibilidade12(dividendo)
    elif divisor == 15:
        resultado = divisibilidade15(dividendo)
    elif divisor == 25:
        resultado = divisibilidade25(dividendo)
    else:
        resultado = False   # divisor que não está na lista
    return resultado


# ---------- Programa principal ----------
def main():
    # Mostra a mensagem inicial
    imprimirObjetivoLab()

    # Lista dos divisores aceitos
    divisoresValidos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 25]

    resposta = "s"            # começa em "s" para entrar no laço
    while resposta == "s":    # repete enquanto o usuário quiser testar de novo
        print()
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))

        # Enquanto o divisor não for válido, pede os valores de novo
        while divisor not in divisoresValidos:
            print("Divisor invalido! Favor informar novos valores.")
            print()
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))

        # Testa e mostra o resultado
        if testarDivisibilidade(dividendo, divisor):
            print(dividendo, "eh divisivel por", divisor)
        else:
            print(dividendo, "NAO eh divisivel por", divisor)

        # Pergunta se quer fazer outro teste
        print()
        resposta = input("Deseja realizar novo teste (s/n)? ").lower()

        # Enquanto não responder s ou n, pergunta de novo
        while resposta != "s" and resposta != "n":
            print()
            resposta = input("Opcao invalida! Deseja realizar novo teste (s/n)? ").lower()


# Inicia o programa
main()
