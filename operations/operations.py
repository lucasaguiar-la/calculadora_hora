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

    def add_expenses(self):
        expense_name = "Aluguel"
        expense_value = 500
        self.expenses[expense_name] = expense_value
        self.terminal_window.append_output(f"Despesa '{expense_name}' adicionada com valor de R$ {expense_value:.2f}")

    def add_salary(self):
        self.salary = 3000
        self.terminal_window.append_output(f"Meta salarial atualizada para R$ {self.salary:.2f}")

    def add_events(self):
        self.events = 200
        self.terminal_window.append_output(f"Valor para imprevistos definido como R$ {self.events:.2f}")

    def add_hours(self):
        self.hours = 160
        self.terminal_window.append_output(f"Horas mensais definidas como {self.hours}h")
    #🔸 [Visualização dos registros pelo temrinal]
    '''def view_records():
        print("\n[DESPESAS]")
        for name, value in Operations.expenses.items():
            print(f"Despesa: {name}\nValor: R${value:.2f}")

        print("\n[SALÁRIO]")
        print(f"Meta salarial: R$ {Operations.salary:.2f}")

        print("\n[IMPREVISTOS]")
        print(f"Valor total para imprevistos: R$ {Operations.events:.2f}")

        print("\n[HORAS]")
        print(f"Horas mensais trabalhadas: {Operations.hours}h")

        return'''

    def make_formula(self):
        if not all([self.expenses, self.salary, self.events, self.hours]):
            self.terminal_window.append_output("Preencha todos os valores antes de calcular.")
            return

        total_expenses = sum(self.expenses.values())
        result = (total_expenses + self.salary + self.events) / self.hours
        self.terminal_window.append_output(f"O valor da sua hora de trabalho é de R$ {result:.2f}")

#🔸 [Menu de opções pelo terminal]
    '''def menu(option = 0):
        while option != 7:
            print(
"scolha uma opção:
1) [DESPESAS] - Registrar despesas mensais
2) [SALÁRIO] - Definir meta salarial
3) [IMPREVISTOS] - Definir valor geral para imprevistos
4) [HORAS] - Definir meta de horas a trabalhar
5) Visualizar registros
6) Quanto vale minha hora?
7) Sair
"
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
        return'''
