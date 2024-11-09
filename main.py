global option
global expenses

class Operations:
    expenses = {}

    @staticmethod
    def add_expenses():
        expense_name = str(input("\nDigite um nome para sua despesa: "))
        expense_value = float(input("Qual o valor dessa despesa? "))

        print(f"\nDespesa: {expense_name}\nValor: R$ {expense_value:.2f}")
        answer = str(input("Deseja adicionar essa despesa? [S/N] \n"))
        if answer.upper() == "S":
            Operations.expenses[expense_name] = expense_value
        elif answer.upper() == "N":
            return
        else:
            print("Opção inválida!")
            Operations.add_expenses()
    
    @staticmethod
    def add_salary():
        ...

def menu(option = 0):
    while option != 6:
        print(
'''
Escolha uma opção:
1) Registrar despesas mensais
2) Definir meta salarial
3) Definir valor geral para imprevistos
4) Definir meta de horas a trabalhar
5) Visualizar despesas mensais
6) Sair
'''
        )
        option = int(input())
        match(option):
            case 1:
                Operations.add_expenses()
            case 2:
                print("Opção 2")
            case 3:
                print("Opção 3")
            case 4:
                print("Opção 4")
            case 5:
                for name, value in Operations.expenses.items():
                    print(f"\nDespesa: {name}\nValor: R${value:.2f}")
    return

if __name__ == '__main__':
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    menu()
