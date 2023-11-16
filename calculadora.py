soma = "a"
sub = "b"
mult = "c"
div = "d"

def continuar():
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
    print(f"\n{n1} + {n2} = {calc}\n")
    # todo formatar saída de dados parta não exibir decimal caso não existe


def subtrair(n1, n2):
    calc = n1 - n2
    print(f"\n{n1} - {n2} = {calc}\n")
    # todo formatar saída de dados parta não exibir decimal caso não existe


def multiplicar(n1, n2):
    calc = n1 * n2
    print(f"\n{n1} x {n2} = {calc}\n")
    # todo formatar saída de dados parta não exibir decimal caso não existe


def dividir(n1, n2):
    calc = n1 / n2
    print(f"\n{n1} / {n2} = {calc}\n")
    # todo formatar saída de dados parta não exibir decimal caso não existe


# --- execução ----
continuar()
