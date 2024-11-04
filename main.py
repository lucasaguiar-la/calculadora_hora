
expense_list = []

def questions(option):
    match(option):
        case 1:
            expense = input(str("Dê um nome para sua despesa: "))
            expense_list.append(expense)
        case 2:
            salary = input(float("Qual salário você gostaria de ter? "))
            return salary
        case 3:
            events = input(float("Considere um valor total para imprevistos: "))
            return events
        case 4:
            working_hours = input(int("Quantas horas mensais você pretende trabalhar? "))
            return working_hours

def calculate():
    ...

if __name__ == '__main__':
    ...