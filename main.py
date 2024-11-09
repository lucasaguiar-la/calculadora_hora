global option
global expenses
global salary
global events
global hours

class Operations:
    expenses = {}
    salary = 0
    events = 0
    hours = 1

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
        event_value = int(input("\nDefina um valor total para reserva de emergência: R$"))

        Operations.events = event_value
        print(f"O valor total da sua reserva para imprevistos é de R$ {event_value:.2f}")

    @staticmethod
    def add_hours():
        hours_value = int(input("\nQuantas horas mensais você deseja trabalhar? "))

        Operations.hours = hours_value
        print(f"Horas mensais trabalhadas atualizado para {hours_value}h")

    def view_records():
        print("\n[DESPESAS]")
        for name, value in Operations.expenses.items():
            print(f"Despesa: {name}\nValor: R${value:.2f}")

        print("\n[SALÁRIO]")
        print(f"Meta salarial: R$ {Operations.salary:.2f}")

        print("\n[IMPREVISTOS]")
        print(f"Valor total para imprevistos: R$ {Operations.events:.2f}")

        print("\n[HORAS]")
        print(f"Horas mensais trabalhadas: {Operations.hours}h")

        return

    def make_formula():
        total_expenses = sum(Operations.expenses.values())
        final_salary = Operations.salary
        total_events = Operations.events
        final_hours = Operations.hours

        missing_values = []

        if total_expenses == 0:
            missing_values.append("despesas")
        if final_salary == 0:
            missing_values.append("salário")
        if total_events == 0:
            missing_values.append("imprevistos")
        if final_hours == 0 or final_hours == 1:
            missing_values.append("horas")

        if missing_values:
            print("\nOs seguintes valores estão faltando:")
            for item in missing_values:
                print(f"- {item.capitalize()}")
            print("Por favor, preencha todos os valores antes de calcular.")
        else:
            result = (total_expenses + final_salary + total_events) / final_hours
            print(f"\nO valor da sua hora/trabalho é de R$ {result}")

def menu(option = 0):
    while option != 7:
        print(
'''
Escolha uma opção:
1) [DESPESAS] - Registrar despesas mensais
2) [SALÁRIO] - Definir meta salarial
3) [IMPREVISTOS] - Definir valor geral para imprevistos
4) [HORAS] - Definir meta de horas a trabalhar
5) Visualizar registros
6) Quanto vale minha hora?
7) Sair
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
                Operations.view_records()
            case 6:
                Operations.make_formula()

    return

if __name__ == '__main__':
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    menu()
