import sys
from PyQt5.QtWidgets import QApplication
from gui.terminal_view import TerminalWindow

def main():
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print("\n" + "="*25)
    print("[CALCULADORA VALOR/HORA]")
    print("="*25)

    main()
