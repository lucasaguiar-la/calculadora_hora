import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow, QHBoxLayout)
from PyQt5.QtCore import QProcess
from operations.operations import Operations

class Window(QMainWindow):
    def __init__(self):
        # Inicializar a janela
        super().__init__()
        self.setWindowTitle("Calculadora hora/valor")
        self.resize(200, 350)

        self.load_stylesheet("./style/style.css")
        layout = QVBoxLayout()

        # Botões para cada operação
        button_layout = QVBoxLayout()

        self.expense_button = QPushButton("Registrar Despesas", self)
        self.expense_button.clicked.connect(lambda: Operations.add_expenses(self))
        button_layout.addWidget(self.expense_button)

        self.salary_button = QPushButton("Definir Meta Salarial", self)
        self.salary_button.clicked.connect(lambda: Operations.add_salary(self))
        button_layout.addWidget(self.salary_button)

        self.events_button = QPushButton("Definir Imprevistos", self)
        self.events_button.clicked.connect(lambda: Operations.add_events(self))
        button_layout.addWidget(self.events_button)

        self.hours_button = QPushButton("Definir Horas de Trabalho", self)
        self.hours_button.clicked.connect(lambda: Operations.add_hours(self))
        button_layout.addWidget(self.hours_button)

        self.view_button = QPushButton("Visualizar Registros", self)
        self.view_button.clicked.connect(lambda: Operations.view_records(self))
        button_layout.addWidget(self.view_button)

        self.formula_button = QPushButton("Quanto vale minha hora?", self)
        self.formula_button.clicked.connect(lambda: Operations.make_formula(self))
        button_layout.addWidget(self.formula_button)

        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.process = QProcess(self)
        self.process.setProgram("bash" if sys.platform != "win32" else "cmd")
        self.process.readyReadStandardOutput.connect(self.update_output)
        self.process.start()

    def load_stylesheet(self, filename):
        with open(filename, "r") as file:
            self.setStyleSheet(file.read())

    def update_output(self):
        output = self.process.readAllStandardOutput().data().decode()

