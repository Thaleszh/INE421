import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QAction, qApp, 
    QApplication, QLineEdit, QInputDialog, QGridLayout)
from PyQt5.QtGui import QIcon


class main_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        # file bar actions

        new_automata = QAction(QIcon('new.png'), '&New AF', self)
        new_automata.setShortcut('Ctrl+N')
        new_automata.setStatusTip('Create new Finite Automata')

        new_expression = QAction(QIcon('new.png'), '&New RE', self)
        new_expression.setShortcut('Ctrl+Shift+N')
        new_expression.setStatusTip('Create new regular expression')
        new_expression.triggered.connect(self.new_re)

        exit_action = QAction(QIcon('exit.png'), '&Exit', self)        
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)


        # edit bar actions


        #self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu('&File')
        file_menu.addAction(new_automata)
        file_menu.addAction(new_expression)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu('&Edit')
        
        self.setGeometry(300, 300, 640, 400)
        self.setWindowTitle('Trabalho I')    
        self.show()
    
    def new_re(self, owner):
        self.expression, ok = QInputDialog.getText(self, 'RE Input', 'Enter the Regular Expression: ')
        if ok:
            re = QLabel('Regular Expression: ' + str(self.expression))




        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())  
