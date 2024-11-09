import sys
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow, QTextEdit
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

        self.start_button = QPushButton("Iniciar Operações", self)
        self.start_button.clicked.connect(self.start_operations)
        layout = QVBoxLayout()
        layout.addWidget(self.terminal_view)
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.process = QProcess(self)
        self.process.setProgram("bash" if sys.platform != "win32" else "cmd")
        self.process.readyReadStandardOutput.connect(self.update_output)
        self.process.start()

    def start_operations(self):
        Operations.menu()

    def update_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.terminal_view.append(output)
