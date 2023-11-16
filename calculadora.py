soma = "a"
sub = "b"
mult = "c"
div = "d"


# Laço que mantém o programa em execução enquanto o usuário responder s;
# Se for a primeira rodada, não questiona o usuário sobre realizar novo cálculo.
def executar():
    primeira_rodada = True
    while ( True ):
        if (primeira_rodada):
            primeira_rodada = False
            operacao()

        proxima_rodada = input("Quer realizar outro cálculo? (s ou n) ").lower()
        if ( proxima_rodada == "s"):
            operacao()
        else:
            print("---- ENCERRANDO A CALCULADORA ----")
            break


# Exibe menu e pergunta a operação matemática desejada;
# Se a operação escolhida for válida, chama a função valores.
def operacao():
    print("---- C A L C U L A D O R A ----")
    print("---- Operações Matemáticas ----")
    print("- A : SOMA                    -")
    print("- B : SUBTRAÇÃO               -")
    print("- C : MULTIPLICAÇÃO           -")
    print("- D : DIVISÃO                 -")
    op = input("Qual a operação matemática desejada? ").lower()
    if ( (op == soma) or (op == sub) or (op == mult) or (op == div) ):
        valores(op)
    else:
        print("--- OPÇÃO INVÁLIDA ---")


# Pergunta os valores e chama a função da operação matemática passando os valores
def valores(op):
    n1 = float(input("Informe o primeiro valor: "))
    n2 = float(input("Informe o segundo valor: "))
    print("--- RESULTADO ---")
    if ( op == soma ):
        somar(n1, n2)
    elif ( op == sub ):
        subtrair(n1, n2)
    elif ( op == mult ):
        multiplicar(n1, n2)
    else:
        dividir(n1, n2)


def somar(n1, n2):
    calc = n1 + n2
    print(f"\n{formatar_numero(n1)} + {formatar_numero(n2)} = {formatar_numero(calc)}\n")


def subtrair(n1, n2):
    calc = n1 - n2
    print(f"\n{formatar_numero(n1)} - {formatar_numero(n2)} = {formatar_numero(calc)}\n")


def multiplicar(n1, n2):
    calc = n1 * n2
    print(f"\n{formatar_numero(n1)} x {formatar_numero(n2)} = {formatar_numero(calc)}\n")


def dividir(n1, n2):
    calc = n1 / n2
    print(f"\n{formatar_numero(n1)} / {formatar_numero(n2)} = {formatar_numero(calc)}\n")



# Para que a EXIBIÇAO dos números aconteça sem casas decimais quando for int ou com casas decimais quando for float
def formatar_numero(num):
    if ( num % 1 == 0 ):
        num_formatado = f"{num:.0f}"
    else:
        num_formatado = f"{num}"
    return num_formatado


# --- chamada para execução do programa ----
executar()
