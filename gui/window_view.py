import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow)
from PyQt5.QtCore import QProcess
from operations.operations import Operations

class Window(QMainWindow):
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
        self.events_button.clicked.connect(lambda: Operations.add_events(self))
        layout.addWidget(self.events_button)

        self.hours_button = QPushButton("Definir Horas de Trabalho", self)
        self.hours_button.clicked.connect(lambda: Operations.add_hours(self))
        layout.addWidget(self.hours_button)

        self.view_button = QPushButton("Visualizar Registros", self)
        self.view_button.clicked.connect(lambda: Operations.view_records(self))
        layout.addWidget(self.view_button)

        self.formula_button = QPushButton("Quanto vale minha hora?", self)
        self.formula_button.clicked.connect(lambda: Operations.make_formula(self))
        layout.addWidget(self.formula_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.process = QProcess(self)
        self.process.setProgram("bash" if sys.platform != "win32" else "cmd")
        self.process.readyReadStandardOutput.connect(self.update_output)
        self.process.start()

    def update_output(self):
        output = self.process.readAllStandardOutput().data().decode()

