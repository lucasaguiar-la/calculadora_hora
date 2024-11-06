
def start():
    expenses = float(input("Qual o seu gasto mensal total? "))
    salary = float(input("Qual a sua meta salarial? "))
    events = float(input("Considere um valor total para imprevistos: "))
    working_hours = int(input("Quantas horas mensais você deseja fazer? "))

    formula = (expenses + salary + events) / working_hours

    print(f'''
        Gastos mensais totais: R$ {float(expenses):.2f}\n
        Meta salarial: R$ {float(salary):.2f}\n
        Valor para imprevisto: R$ {float(events):.2f}\n
        Horas trabalhadas: {float(working_hours)}\n
        ====================================================\n
        Valor da hora trabalhada: R$ {formula:.2f}
    ''')

if __name__ == '__main__':
    start()