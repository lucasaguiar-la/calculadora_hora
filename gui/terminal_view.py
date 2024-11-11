import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow, 
                            QTextEdit, QLineEdit, QLabel, QMessageBox, QInputDialog)
from PyQt5.QtCore import QProcess
from operations.operations import Operations

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora hora/valor")
        self.resize(800, 600)

        self.terminal_view = QTextEdit(self)
        self.terminal_view.setReadOnly(True)
        self.setCentralWidget(self.terminal_view)

        self.init_ui()

        self.operations = Operations()

    def init_ui(self):
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)

        layout.addWidget(self.terminal_view)

        btn_expense = QPushButton("Adicionar Despesa", self)
        btn_salary = QPushButton("Definir Meta Salarial", self)
        btn_events = QPushButton("Definir Valor para Imprevistos", self)
        btn_hours = QPushButton("Definir Horas de Trabalho", self)
        btn_calculate = QPushButton("Calcular Valor/Hora", self)

        btn_expense.clicked.connect(self.operations.add_expenses)
        btn_salary.clicked.connect(self.operations.add_salary)
        btn_events.clicked.connect(self.operations.add_events)
        btn_hours.clicked.connect(self.operations.add_hours)
        btn_calculate.clicked.connect(self.operations.make_formula)

        layout.addWidget(btn_expense)
        layout.addWidget(btn_salary)
        layout.addWidget(btn_events)
        layout.addWidget(btn_hours)
        layout.addWidget(btn_calculate)

        self.setCentralWidget(container)
