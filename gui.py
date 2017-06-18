import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from Finite_Automata import Finite_Automata
import FA_Algorithms

class gui():

	def __init__(self):
		self.FA_list = []
		self.RE_list = []
		self.current_fa = None
		self.initUI()

	def initUI(self):

		# main window
		self.main_window = QMainWindow()
		self.main_window.resize(800, 600)

		self.central_widget = QWidget()

		#layout
		self.grid = QGridLayout(self.central_widget)
		self.grid.setColumnStretch(1, 4)
		self.grid.setColumnStretch(2, 4)
		self.grid.setSpacing(5)

        # -- menu bar --
		self.menubar = self.main_window.menuBar()
		self.menubar.setNativeMenuBar(False)

		# file bar actions
		self.file_menu = self.menubar.addMenu('&File')

		self.new_automata = QAction(QIcon('new.png'), '&New FA', self.main_window)
		self.new_automata.setShortcut('Ctrl+N')
		self.new_automata.setStatusTip('Create new Finite Automata')
		self.new_automata.triggered.connect(self.new_fa)
		self.file_menu.addAction(self.new_automata)

		self.new_expression = QAction(QIcon('new.png'), '&New RE', self.main_window)
		self.new_expression.setShortcut('Ctrl+Shift+N')
		self.new_expression.setStatusTip('Create new regular expression')
		self.new_expression.triggered.connect(self.new_re)
		self.file_menu.addAction(self.new_expression)

		self.exit_action = QAction(QIcon('exit.png'), '&Exit', self.main_window)        
		self.exit_action.setShortcut('Ctrl+Q')
		self.exit_action.setStatusTip('Exit application')
		self.exit_action.triggered.connect(qApp.quit)
		self.file_menu.addAction(self.exit_action)

		# edit menu bar actions
		self.edit_menu = self.menubar.addMenu('&Edit')

		self.close = QAction(QIcon('state.png'), '&Close Tab', self.main_window)
		#self.close.setShortcut('Ctrl+S')
		self.close.setStatusTip('Closes current tb')
		self.close.triggered.connect(self.close_event)
		self.edit_menu.addAction(self.close)

		# FA options:
		self.new_state = QAction(QIcon('state.png'), '&Create State', self.main_window)
		self.new_state.setShortcut('Ctrl+S')
		self.new_state.setStatusTip('Creates new state to current FA')
		self.new_state.triggered.connect(self.create_state_event)
		self.edit_menu.addAction(self.new_state)

		self.delete_state = QAction(QIcon('state.png'), '&Delete State', self.main_window)
		self.delete_state.setShortcut('Ctrl+Shift+S')
		self.delete_state.setStatusTip('Deletes a state in current FA')
		self.delete_state.triggered.connect(self.delete_state_event)
		self.edit_menu.addAction(self.delete_state)

		self.create_transition = QAction(QIcon('state.png'), '&Create Transition', self.main_window)
		self.create_transition.setShortcut('Ctrl+T')
		self.create_transition.setStatusTip('Creates new transition to current FA')
		self.create_transition.triggered.connect(self.create_transition_event)
		self.edit_menu.addAction(self.create_transition)

		self.delete_transition = QAction(QIcon('state.png'), '&Delete Transition', self.main_window)
		self.delete_transition.setShortcut('Ctrl+Shift+T')
		self.delete_transition.setStatusTip('Deletes a transition in current FA')
		self.delete_transition.triggered.connect(self.delete_transition_event)
		self.edit_menu.addAction(self.delete_transition)

		self.unite = QAction(QIcon('state.png'), '&Union', self.main_window)
		self.unite.setShortcut('Ctrl+U')
		self.unite.setStatusTip('Unites an FA with another one FA')
		self.unite.triggered.connect(self.union_event)
		self.edit_menu.addAction(self.unite)

		self.intersection = QAction(QIcon('state.png'), '&Intersection', self.main_window)
		self.intersection.setShortcut('Ctrl+I')
		self.intersection.setStatusTip('Intersects an FA with another one FA')
		self.intersection.triggered.connect(self.intersection_event)
		self.edit_menu.addAction(self.intersection)

		self.complement = QAction(QIcon('state.png'), '&Complement', self.main_window)
		self.complement.setShortcut('Ctrl+Shift+C')
		self.complement.setStatusTip('Complements current FA')
		self.complement.triggered.connect(self.complement_event)
		self.edit_menu.addAction(self.complement)

		self.diff = QAction(QIcon('state.png'), '&Difference', self.main_window)
		self.diff.setShortcut('Ctrl+Shift+C')
		self.diff.setStatusTip('Makes the difference of an FA with a second FA')
		self.diff.triggered.connect(self.diff_event)
		self.edit_menu.addAction(self.diff)

		self.minimize = QAction(QIcon('state.png'), '&Minimize', self.main_window)
		self.minimize.setShortcut('Ctrl+Shift+M')
		self.minimize.setStatusTip('Minimizes the current FA')
		self.minimize.triggered.connect(self.minimize_event)
		self.edit_menu.addAction(self.minimize)

		self.determinize = QAction(QIcon('state.png'), '&Determinize', self.main_window)
		self.determinize.setShortcut('Ctrl+Shift+D')
		self.determinize.setStatusTip('Determinizes the current FA')
		self.determinize.triggered.connect(self.determinize_event)
		self.edit_menu.addAction(self.determinize)
		self.allow_FA(0)

		# tab

		self.tabs = QTabWidget(self.central_widget)
		self.tabs.resize(800,600)
		self.central_widget

		self.tabs.currentChanged.connect(self.tab_changed)

		self.main_window.setCentralWidget(self.central_widget)

		self.main_window.setGeometry(300,300,800,600)
		self.main_window.show()

		self.create_fa('m1', 'abcd')
		self.create_state('q0', True, True)

	def allow_FA(self, boolea):
		if boolea:
			self.determinize.setEnabled(True)
			self.minimize.setEnabled(True)
			self.diff.setEnabled(True)
			self.complement.setEnabled(True)
			self.intersection.setEnabled(True)
			self.unite.setEnabled(True)
			self.delete_transition.setEnabled(True)
			self.delete_state.setEnabled(True)
			self.create_transition.setEnabled(True)
			self.new_state.setEnabled(True)
			self.close.setEnabled(True)
		else:
			self.determinize.setEnabled(False)
			self.minimize.setEnabled(False)
			self.diff.setEnabled(False)
			self.complement.setEnabled(False)
			self.intersection.setEnabled(False)
			self.unite.setEnabled(False)
			self.delete_transition.setEnabled(False)
			self.delete_state.setEnabled(False)
			self.create_transition.setEnabled(False)
			self.new_state.setEnabled(False)
			self.close.setEnabled(False)

	# closes current tab
	def close_event(self):
		pass

	def tab_changed(self):
		current_tab = self.tabs.currentWidget()
		if current_tab.type == 'FA':
			self.allow_FA(True)
			for fa in self.FA_list:
					if fa.name == current_tab.name:
						self.current_fa = fa
						break
		else:
			self.allow_FA(False)

	def create_state_event(self):
		state_name, ok = QInputDialog.getText(self.main_window, 'Create State', 'Name the state:')
		if ok:
			is_final = QMessageBox.question(self.main_window, 'Final?', 'Is the state final?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			is_initial = QMessageBox.question(self.main_window, 'Final?', 'Is the state initial?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
			if is_initial == QMessageBox.Yes:
				is_initial = True
			else:
				is_initial = False
			if is_final == QMessageBox.Yes:
				is_final = True
			else:
				is_final = False
			create_state(state_name, is_final, is_initial)

	def create_state(self, state_name, is_final, is_initial):
		current_tab = self.tabs.currentWidget()
		if self.current_fa is None or self.current_fa.name != current_tab.name:				
			for fa in self.FA_list:
				if fa.name == current_tab.name:
					self.current_fa = fa
					break
		self.current_fa.create_state(state_name, is_initial, is_final)
		self.update_table()

	def create_transition_event(self):
		create_transition_text, ok = QInputDialog.getText(self.main_window, 'Create Transition', 'Choose the automata')

		if ok:
			pass

	def delete_state_event(self):
		delete_state_text, ok = QInputDialog.getText(self.main_window, 'Delete State', 'Choose the automata')

		if ok:
			pass

	def delete_transition_event(self):
		delete_transition_text, ok = QInputDialog.getText(self.main_window, 'Delete Transition', 'Choose the automata')

		if ok:
			pass

	def union_event(self):
		union_text1, ok = QInputDialog.getText(self.main_window, 'Union', 'Choose the first automata')

		if ok:
			self.le1.setText(str(union_text1))

		union_text2, ok = QInputDialog.getText(self.main_window, 'Union', 'Choose the second automata')

		if ok:
			self.le2.setText(str(union_text2))

	def intersection_event(self):
		intersection_text1, ok = QInputDialog.getText(self.main_window, 'Intersection','Choose the first automata')

		if ok:
			self.le1.setText(str(union_text1))

		intersection_text2, ok = QInputDialog.getText(self.main_window, 'Intersection', 'Choose the second automata')

		if ok:
			self.le2.setText(str(union_text2))

	def complement_event(self):
		complement_text, ok = QInputDialog.getText(self.main_window, 'Complement', 'Choose the automata')

		if ok:
			pass

	def diff_event(self):
		diff_text1, ok = QInputDialog.getText(self.main_window, 'Difference', 'Choose the first automata')

		if ok:
			self.le1.setText(str(union_text1))

		diff_text2, ok = QInputDialog.getText(self.main_window, 'Difference', 'Choose the second automata')

		if ok:
			self.le2.setText(str(union_text2))

	def minimize_event(self):
		minimize_text, ok = QInputDialog.getText(self.main_window, 'Minimize', 'Choose the automata')

		if ok:
			pass

	def determinize_event(self):
		determinize_text, ok = QInputDialog.getText(self.main_window, 'Determinize', 'Choose the automata')

		if ok:
			pass

	def new_fa(self):
		self.expression, ok = QInputDialog.getText(self.main_window, 'FA Input', 'Enter the name of the Finite Automata: ')
		if ok:
			alphabet, ok = QInputDialog.getText(self.main_window, 'Alphabet Input', 'Enter the alphabet of ' + self.expression)
			self.create_fa(expression, alphabet)

	def create_fa(self, expression, alphabet):
		new_FA = Finite_Automata()
		new_FA.set_name(str(expression))
		self.FA_list.append(new_FA)
		self.add_tab(expression, ['FA', alphabet])

	def new_re(self):
		self.expression, ok = QInputDialog.getText(self.main_window, 'RE Input', 'Enter the name of the Regular Expression: ')
		if ok:
			re = QLabel('Regular Expression: ' + str(self.expression))

	def cell_changed_event(self, row, column):
		current_tab = self.tabs.currentWidget()
		current_item = current_tab.table_widget.item(row, column)

		if current_item.text() != '' :
			self.current_fa.create_transition(current_tab.states[row], current_item.text() , current_tab.characters[column])
		#might have added new state
		self.update_table()

	def update_table(self):
		current_tab = self.tabs.currentWidget()
		#current_tab.table_widget.setColumnCount(len(current_tab.characters))
		#current_tab.table_widget.setHorizontalHeaderLabels(current_tab.characters)
		if len(current_tab.states) != len(self.current_fa.states):
			current_tab.table_widget.setRowCount(len(self.current_fa.states))
			current_tab.states.clear()
			current_tab.states_extra.clear()
			name = ''
			for state in self.current_fa.states:
				name = state
				extra = ''
				if state in self.current_fa.finals:
					extra += '*'
				if state == self.current_fa.initials:
					extra += '->'
				current_tab.states.append(name)
				current_tab.states_extra.append(extra)
		names = list()
		i = 0
		while i < len(current_tab.states):
			names.append(current_tab.states_extra[i] + current_tab.states[i])
			i += 1
		current_tab.table_widget.setVerticalHeaderLabels(names)

	def add_tab(self, tab_name, tab_type):
		new_tab = Tab(tab_name, tab_type)
		self.tabs.addTab(new_tab, tab_name)
		new_tab.table_widget.cellChanged.connect(self.cell_changed_event)

class Tab(QWidget):
	def __init__(self, tab_name, tab_type):
		super().__init__()
		self.name = tab_name
		self.type = tab_type[0]
		self.characters = list()
		self.table_widget = QTableWidget()
		self.states = list()
		self.states_extra = list()
		self.layout = QVBoxLayout(self)
		if self.type == 'FA':
			self.characters = list()
			for character in tab_type[1]:
				self.characters.append(character)
			self.table_widget.setColumnCount(len(self.characters))
			self.table_widget.setHorizontalHeaderLabels(self.characters)
			self.layout.addWidget(self.table_widget)
			self.setLayout(self.layout)

if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = gui()
	sys.exit(app.exec_())  
