import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Simple Example')
        
        # Membuat label
        self.label = QLabel('Enter your name:', self)
        
        # Membuat kotak teks
        self.textbox = QLineEdit(self)
        
        # Membuat tombol
        self.btn = QPushButton('Submit', self)
        self.btn.clicked.connect(self.showDialog)
        
        # Menyusun layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.btn)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        name = self.textbox.text()
        QMessageBox.information(self, 'Message', f'Hello, {name}!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
  
