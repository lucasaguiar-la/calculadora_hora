
def menu():
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    option = int(input('''
Escolha uma opção:
1) Registrar despesas mensais
2) Definir meta salarial
3) Definir valor geral para imprevistos
4) Definir meta de horas a trabalhar
5) Sair\n
'''))
    return option

if __name__ == '__main__':
    option = menu()
    while option != 5:
        menu()