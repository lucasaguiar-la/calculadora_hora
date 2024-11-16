from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow, QTextEdit, QLineEdit, QLabel, QMessageBox, QInputDialog)

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
    def add_expenses(parent):
        expense_name, ok1 = QInputDialog.getText(parent, 'Adicionar Despesa', 'Digite um nome para sua despesa:')
        print(expense_name)
        if ok1:
            expense_value, ok2 = QInputDialog.getDouble(parent, 'Adicionar Despesa', 'Qual o valor dessa despesa?')
            print(expense_value + "\n")
            if ok2:
                Operations.expenses[expense_name] = expense_value
                QMessageBox.information(parent, 'Despesa Adicionada', f"Despesa: {expense_name}\nValor: R$ {expense_value:.2f}")
                print(f"Despesa: {expense_name}\nValor: R$ {expense_value:.2f}")

    @staticmethod
    def add_salary(parent):
        salary_value, ok = QInputDialog.getDouble(parent, 'Definir Meta Salarial', 'Qual sua meta salarial?')
        if ok:
            Operations.salary = salary_value
            QMessageBox.information(parent, 'Meta Salarial Definida', f"Meta salarial atualizada para R$ {salary_value}")

    @staticmethod
    def add_events(parent):
        event_value, ok = QInputDialog.getDouble(parent, 'Definir Imprevistos', 'Defina um valor total para reserva de emergência:')
        if ok:
            Operations.events = event_value
            QMessageBox.information(parent, 'Imprevistos Definidos', f"O valor total da sua reserva para imprevistos é de R$ {event_value:.2f}")

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
                case 7:
                    return
        return
