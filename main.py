import sys
from PyQt5.QtWidgets import QApplication
from gui.window_view import Window

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print("APLICAÇÃO INICIADA")
    main()
