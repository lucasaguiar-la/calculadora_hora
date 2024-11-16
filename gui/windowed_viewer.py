import sys
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit, QLabel, QMessageBox)
from operations.operations import Operations

class Window(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowIcon(self.style().standardIcon(0))
        self.setWindowTitle("Calculadora de Valor/Hora")
        self.resize(400, 450)

        self.expenses = {}
        self.operations = Operations(self)
        self.init_ui()

    def expenses(self):
        self.btn_expense = QPushButton("Adicionar Despesa", self)
        self.btn_expense.clicked.connect(self.show_expense_inputs)

        self.main_layout.addWidget(self.btn_expense)

        self.expense_name_input = QLineEdit(self)
        self.expense_value_input = QLineEdit(self)
        self.expense_save_button = QPushButton("Salvar Despesa", self)

        self.expense_name_input.setPlaceholderText("Nome da despesa")
        self.expense_value_input.setPlaceholderText("Valor da despesa (em R$)")

        self.expense_save_button.clicked.connect(self.save_expense)

    def show_expense_inputs(self):
        self.main_layout.addWidget(QLabel("Nome da Despesa:"))
        self.main_layout.addWidget(self.expense_name_input)
        self.main_layout.addWidget(QLabel("Valor da Despesa:"))
        self.main_layout.addWidget(self.expense_value_input)
        self.main_layout.addWidget(self.expense_save_button)

        self.expense_name_input.show()
        self.expense_value_input.show()
        self.expense_save_button.show()
    
    def save_expense(self):
        expense_name = self.expense_name_input.text()
        expense_value = self.expense_value_input.text()

        if expense_name and expense_value.replace(',', '').replace('.', '').isdigit():
            expense_value = float(expense_value.replace(',', '.'))
            self.expenses[expense_name] = expense_value

            QMessageBox.information(self, "Despesa Salva", f"Despesa '{expense_name}' de R$ {expense_value:.2f} salva com sucesso!")

            self.expense_name_input.clear()
            self.expense_value_input.clear()
            self.expense_name_input.hide()
            self.expense_value_input.hide()
            self.expense_save_button.hide()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira um nome válido e um valor numérico para a despesa.")


    def init_ui(self):
        self.main_layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)

        Window.expenses(self)

        
        #btn_salary = QPushButton("Definir Meta Salarial", self)
        #btn_events = QPushButton("Definir Valor para Imprevistos", self)
        #btn_hours = QPushButton("Definir Horas de Trabalho", self)
        #btn_calculate = QPushButton("Calcular Valor/Hora", self)

        
        #layout.addWidget(btn_salary)
        #layout.addWidget(btn_events)
        #layout.addWidget(btn_hours)
        #layout.addWidget(btn_calculate)
