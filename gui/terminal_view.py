import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow, QTextEdit, QLineEdit, QLabel, QMessageBox, QInputDialog)
from PyQt5.QtCore import QProcess
from operations.operations import Operations

class TerminalWindow(QMainWindow):
    def __init__(self):
        # Inicializar a janela
        super().__init__()
        self.setWindowTitle("Calculadora hora/valor")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Botões para cada operação
        self.expense_button = QPushButton("Registrar Despesas", self)
        self.expense_button.clicked.connect(lambda: Operations.add_expenses(self))
        layout.addWidget(self.expense_button)

        self.salary_button = QPushButton("Definir Meta Salarial", self)
        self.salary_button.clicked.connect(lambda: Operations.add_salary(self))
        layout.addWidget(self.salary_button)

        self.events_button = QPushButton("Definir Imprevistos", self)
        self.events_button.clicked.connect(self.add_events)
        layout.addWidget(self.events_button)

        self.hours_button = QPushButton("Definir Horas de Trabalho", self)
        self.hours_button.clicked.connect(self.add_hours)
        layout.addWidget(self.hours_button)

        self.view_button = QPushButton("Visualizar Registros", self)
        self.view_button.clicked.connect(self.view_records)
        layout.addWidget(self.view_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.process = QProcess(self)
        self.process.setProgram("bash" if sys.platform != "win32" else "cmd")
        self.process.readyReadStandardOutput.connect(self.update_output)
        self.process.start()

    def add_events(self):
        # Implementar a lógica para definir imprevistos
        event_value, ok = QInputDialog.getDouble(self, 'Definir Imprevistos', 'Defina um valor total para reserva de emergência:')
        if ok:
            Operations.events = event_value
            #self.terminal_view.append(f"O valor total da sua reserva para imprevistos é de R$ {event_value:.2f}")

    def add_hours(self):
        # Implementar a lógica para definir horas de trabalho
        hours_value, ok = QInputDialog.getInt(self, 'Definir Horas de Trabalho', 'Quantas horas mensais você deseja trabalhar?')
        if ok:
            Operations.hours = hours_value
            #self.terminal_view.append(f"Horas mensais trabalhadas atualizadas para {hours_value}h")

    def view_records(self):
        # Visualizar registros
        records = "\n[DESPESAS]\n"
        for name, value in Operations.expenses.items():
            records += f"Despesa: {name}\nValor: R$ {value:.2f}\n"
        records += f"\n[SALÁRIO]\nMeta salarial: R$ {Operations.salary:.2f}\n"
        records += f"\n[IMPREVISTOS]\nValor total para imprevistos: R$ {Operations.events:.2f}\n"
        records += f"\n[HORAS]\nHoras mensais trabalhadas: {Operations.hours}h\n"
        #self.terminal_view.append(records)

    def update_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        #self.terminal_view.append(output)
