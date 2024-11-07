
def menu(option):
    while option != 5:
        print(
'''
Escolha uma opção:
1) Registrar despesas mensais
2) Definir meta salarial
3) Definir valor geral para imprevistos
4) Definir meta de horas a trabalhar
5) Sair
'''
        )
        option = int(input())
    return

if __name__ == '__main__':
    option = 0

    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    menu(option)
