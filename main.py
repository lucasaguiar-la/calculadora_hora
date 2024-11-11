import sys
from PyQt5.QtWidgets import QApplication
from gui.windowed_viewer import TerminalWindow

def main():
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print("APLICAÇÃO INICIADA")
    main()
