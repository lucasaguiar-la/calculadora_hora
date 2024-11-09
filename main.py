global option
global expenses
global salary
global events
global hours

class Operations:
    expenses = {}
    salary = 0
    events = {}
    hours = 1

    def formula():
        total_expenses = sum(Operations.expenses.values())
        final_salary = Operations.salary
        total_events = sum(Operations.events.values())
        final_hours = Operations.hours

        result = (total_expenses + final_salary + total_events) / final_hours
        print(f"O valor da sua hora/trabalho é de R$ {result}")

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
        salary_value = float(input("\nQual sua meta salarial? "))

        Operations.salary = salary_value
        print(f"Meta salarial atualizada para R$ {salary_value}")

    @staticmethod
    def add_events():
        event_name = str(input("\nAdicione uma tag para esse emprevisto (ex.: Despesas médicas, Oficina etc...): "))
        event_value = float(input("Qual o valor dessa tag? "))

        print(f"\nTag: {event_name}\nValor: R$ {event_value:.2f}")
        answer = str(input("Deseja adicionar essa despesa? [S/N] \n"))
        if answer.upper() == 'S':
            Operations.events[event_name] = event_value
        elif answer.upper() == 'N':
            return
        else:
            print("Opção inválida!")
            Operations.add_events()

    @staticmethod
    def add_hours():
        hours_value = int(input("\nQuantas horas mensais você deseja trabalhar? "))

        Operations.hours = hours_value
        print(f"Horas mensais trabalhadas atualizado para {hours_value}h")

def menu(option = 0):
    while option != 6:
        print(
'''
Escolha uma opção:
1) Registrar despesas mensais
2) Definir meta salarial
3) Definir valor geral para imprevistos
4) Definir meta de horas a trabalhar
5) Visualizar
6) Sair
'''
        )
        option = int(input())
        match(option):
            case 1:
                Operations.add_expenses()
            case 2:
                Operations.add_salary()
            case 3:
                Operations.add_events()
            case 4:
                Operations.add_hours()
            case 5:
                Operations.formula()
                '''print("\n[DESPESAS]")
                for name, value in Operations.expenses.items():
                    print(f"\nDespesa: {name}\nValor: R${value:.2f}")
                print("\n[IMPREVISTOS]")
                for name, value in Operations.events.items():
                    print(f"\nTag: {name}\nValor: R${value:.2f}")'''
    return

if __name__ == '__main__':
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    menu()
