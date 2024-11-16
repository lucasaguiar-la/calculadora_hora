from PyQt5.QtWidgets import (QMessageBox, QInputDialog)

global option
global expenses
global salary
global events
global hours

class Operations:
    def __init__(self, terminal_window):
        self.terminal_window = terminal_window
        self.expenses = {}
        self.salary = 0
        self.events = 0
        self.hours = 1

    @staticmethod
    def add_expenses(parent):
        expense_name, ok1 = QInputDialog.getText(parent, 'Adicionar Despesa', 'Digite um nome para sua despesa:')
        if ok1:
            expense_value, ok2 = QInputDialog.getDouble(parent, 'Adicionar Despesa', 'Qual o valor dessa despesa?')
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
    def add_hours(parent):
        hours_value, ok = QInputDialog.getInt(parent, 'Definir Horas de Trabalho', 'Quantas horas mensais você deseja trabalhar?')
        if ok:
            Operations.hours = hours_value
            QMessageBox.information(parent, 'Horas Definidas', f"Horas mensais trabalhadas atualizado para {hours_value}h")

    @staticmethod
    def view_records(parent):
        records = "\n[DESPESAS]\n"
        for name, value in Operations.expenses.items():
            records += f"Despesa: {name}\nValor: R$ {value:.2f}\n"
        records += f"\n[SALÁRIO]\nMeta salarial: R$ {Operations.salary:.2f}\n"
        records += f"\n[IMPREVISTOS]\nValor total para imprevistos: R$ {Operations.events:.2f}\n"
        records += f"\n[HORAS]\nHoras mensais trabalhadas: {Operations.hours}h\n"
        QMessageBox.information(parent, 'Visualizar Registros', records)

        return

    @staticmethod
    def make_formula(parent):
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
            missing_items = "\n".join(f"- {item.capitalize()}" for item in missing_values)
            QMessageBox.warning(parent, 'Valores Faltando', f"\nOs seguintes valores estão faltando:\n{missing_items}\nPor favor, preencha todos os valores antes de calcular.")
        else:
            result = (total_expenses + final_salary + total_events) / final_hours
            QMessageBox.information(parent, 'Resultado', f"\nO valor da sua hora/trabalho é de R$ {result:.2f}")

