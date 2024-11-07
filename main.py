global option
global expense_list

class Operations:
    def add_expeses():
        expense_name = str(input("Digite um nome para sua despesa: "))
        expense_value = float(input("Qual o valor dessa despesa? "))
        test_list = dict(expense_name, expense_value)
        return test_list 

def menu(option = 0, expense_list=[]):
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
        match(option):
            case 1:
                print("Opção 1")
                expense_list.append(Operations.add_expeses())
                print(expense_list)
            case 2:
                print("Opção 2")
            case 3:
                print("Opção 3")
            case 4:
                print("Opção 4")
    return

if __name__ == '__main__':
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    menu()
