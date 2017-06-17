import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QAction, qApp, 
    QApplication, QLineEdit, QInputDialog, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from Finite_Automata import Finite_Automata
import FA_algorithms

class main_window(QMainWindow):
    
    def __init__(self):
        self.FA_list = []
        self.RE_list = []
        print(self.FA_list)
        super().__init__()
        self.initUI()
        
        
    def initUI(self):               
        #buttons
        createSb = QPushButton('Create State', self)
        createSb.move(200, 200)
        createSb.clicked.connect(self.create_state_button)

        createTb = QPushButton('Create Transition', self)
        createTb.move(200, 230)
        createTbb.clicked.connect(self.create_transition_button)

        deleteSb = QPushButton('Delete State', self)
        deleteSb.move(200, 260)
        deleteSb.clicked.connect(self.delete_state_button)

        deleteTb = QPushButton('Delete Transition', self)
        deleteTb.move(200, 290)
        deleteTb.clicked.connect(self.delete_transition_button)

        unionb = QPushButton('Union', self)
        unionb.move(10, 60)
        unionb.clicked.connect(self.union_button)

        complementb = QPushButton('Complement', self)
        complementb.move(10, 110)
        complementb.clicked.connect(self.complement_button)

        intersectionb = QPushButton('Intersection', self)
        intersectionb.move(10, 160)
        intersectionb.clicked.connect(self.intersection_button)
        
        diffb = QPushButton('Difference', self)
        diffb.move(10, 210)
        diffb.clicked.connect(self.diff_button)
        
        minimizeb = QPushButton('Minimize', self)
        minimizeb.move(10, 260)
        minimizeb.clicked.connect(self.minimize_button)
        
        determinizeb = QPushButton('Determinize', self)
        determinizeb.move(10, 310)
        determinizeb.clicked.connect(self.determinize_button)
      
        listb = QPushButton('listar', self)
        listb.move(150, 150)
        listb.clicked.connect(self.listar)

        self.le1 = QLineEdit(self)
        self.le1.move(130, 22)
        
        self.le2 = QLineEdit(self)
        self.le2.move(130, 72)

        # file bar actions

        new_automata = QAction(QIcon('new.png'), '&New FA', self)
        new_automata.setShortcut('Ctrl+N')
        new_automata.setStatusTip('Create new Finite Automata')
        new_automata.triggered.connect(self.new_fa)

        new_expression = QAction(QIcon('new.png'), '&New RE', self)
        new_expression.setShortcut('Ctrl+Shift+N')
        new_expression.setStatusTip('Create new regular expression')
        new_expression.triggered.connect(self.new_re)

        exit_action = QAction(QIcon('exit.png'), '&Exit', self)        
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

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
    
    def listar(self):
        for fa in self.FA_list:
            print(fa.name)

    def create_state_button(self):
        pass

    def create_transition_button(self):
        pass

    def delete_state_button(self):
        pass

    def create_transition_button(self):
        pass

    def union_button(self):
        union_text1, ok = QInputDialog.getText(self, 'Union', 'Chose the first automata')

        if ok:
            self.le1.setText(str(union_text1))

        union_text2, ok = QInputDialog.getText(self, 'Union', 'Chose the second automata')

        if ok:
            self.le2.setText(str(union_text2))

    def intersection_button(self):
        pass

    def complement_button(self):
        pass

    def minimize_button(self):
        pass

    def determinize_button(self):
        pass

    def new_fa(self, owner):
        self.expression, ok = QInputDialog.getText(self, 'FA Input', 'Enter the Finite Automata: ')
        if ok:
            new_FA = Finite_Automata()
            new_FA.set_name(str(self.expression))
            self.FA_list.append(new_FA)
            print(self.FA_list)
            fa = QLabel('Finite Automata: ' + str(self.expression))

    def new_re(self, owner):
        self.expression, ok = QInputDialog.getText(self, 'RE Input', 'Enter the Regular Expression: ')
        if ok:
            re = QLabel('Regular Expression: ' + str(self.expression))

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())  
