import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QWidget, QAction, qApp, 
    QApplication, QLineEdit, QInputDialog, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from Finite_Automata import Finite_Automata
import FA_Algorithms

class main_window(QMainWindow):
    
    def __init__(self):
        self.FA_list = []
        self.RE_list = []
        super().__init__()
        self.initUI()
        
        
    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(5)


        #buttons
        createSb = QPushButton('Create State', self)
        createSb.clicked.connect(self.create_state_event)

        createTb = QPushButton('Create Transition', self)
        createTb.clicked.connect(self.create_transition_event)

        deleteSb = QPushButton('Delete State', self)
        deleteSb.clicked.connect(self.delete_state_event)

        deleteTb = QPushButton('Delete Transition', self)
        deleteTb.clicked.connect(self.delete_transition_event)

        unionb = QPushButton('Union', self)
        unionb.clicked.connect(self.union_event)

        complementb = QPushButton('Complement', self)
        complementb.clicked.connect(self.complement_event)

        intersectionb = QPushButton('Intersection', self)
        intersectionb.clicked.connect(self.intersection_event)
        
        diffb = QPushButton('Difference', self)
        diffb.clicked.connect(self.diff_event)
        
        minimizeb = QPushButton('Minimize', self)
        minimizeb.clicked.connect(self.minimize_event)
        
        determinizeb = QPushButton('Determinize', self)
        determinizeb.clicked.connect(self.determinize_event)
        
        grid.addWidget(createSb, 1, 0)
        grid.addWidget(createTb, 2, 0)
        grid.addWidget(deleteSb, 3, 0)
        grid.addWidget(deleteTb, 4, 0)
        grid.addWidget(unionb, 5, 0)
        grid.addWidget(complementb, 6, 0)
        grid.addWidget(intersectionb, 7, 0)
        grid.addWidget(diffb, 8, 0)
        grid.addWidget(minimizeb, 9, 0)
        grid.addWidget(determinizeb, 10, 0)

        self.setLayout(grid)
        
        
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

    def create_state_event(self):
        pass

    def create_transition_event(self):
        pass

    def delete_state_event(self):
        pass

    def delete_transition_event(self):
        pass

    def union_event(self):
        union_text1, ok = QInputDialog.getText(self, 'Union', 'Chose the first automata')

        if ok:
            self.le1.setText(str(union_text1))

        union_text2, ok = QInputDialog.getText(self, 'Union', 'Chose the second automata')

        if ok:
            self.le2.setText(str(union_text2))

    def intersection_event(self):
        pass

    def complement_event(self):
        pass

    def diff_event(self):
        pass

    def minimize_event(self):
        pass

    def determinize_event(self):
        pass

    def new_fa(self, owner):
        self.expression, ok = QInputDialog.getText(self, 'FA Input', 'Enter the Finite Automata: ')
        if ok:
            new_FA = Finite_Automata()
            new_FA.set_name(str(self.expression))
            self.FA_list.append(new_FA)
            fa = QLabel('Finite Automata: ' + str(self.expression))

    def new_re(self, owner):
        self.expression, ok = QInputDialog.getText(self, 'RE Input', 'Enter the Regular Expression: ')
        if ok:
            re = QLabel('Regular Expression: ' + str(self.expression))

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())  
